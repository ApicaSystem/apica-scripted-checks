package com.apicasystems.metricsdemo;

import com.apicasystems.metricsdemo.model.JsonResult;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import kong.unirest.Header;
import kong.unirest.HttpResponse;
import kong.unirest.Unirest;

public class Main {

  private static ObjectMapper mapper = new ObjectMapper();

  public static void main(String[] args) throws Exception {
    String url;

    try {
      url = args[0];
    } catch (Exception ignored) {
      url = "https://example.com";
    }

    Unirest.config()
        .concurrency(1, 1)
        .verifySsl(false)
        .automaticRetries(false)
        .socketTimeout(10000)
        .connectTimeout(10000);

    var result = new JsonResult();
    double startTime = System.currentTimeMillis() / 1000.0;
    result.setStartTime(startTime);
    result.setCmd(List.of(url));
    final var httpResponse = callUrl(url);
    double endTime = System.currentTimeMillis() / 1000.0;

    Number duration = endTime - startTime;
    var metricsMap = new HashMap<String, Object>();
    metricsMap.put("http_status", httpResponse.getStatus());
    metricsMap.put("content_size", httpResponse.getBody().length);
    metricsMap.put("header_count", httpResponse.getHeaders().size());
    metricsMap.put("duration", duration.intValue() * 1000);

    result.setEndTime(endTime);
    result.setReturncode(0L);
    result.setStdout("Stdout from java");
    result.setStderr("Stderr from java");
    result.setValue(duration.intValue() + "");
    result.setAdditionalProperties(new HashMap<>(Map.of("metrics", metricsMap)));
    result.setMessage("HTTP Call completed with status " + httpResponse.getStatusText());

    Map<String, String> headers = new HashMap<>();

    for (Header header : httpResponse.getHeaders().all()) {
      headers.put(header.getName(), header.getValue());
    }

    result.getAdditionalProperties().put("headers", headers);
    result.getAdditionalProperties().put("url", url);
    result.getAdditionalProperties().put("java", true);

    Unirest.shutDown();
    printResult(result);
  }

  private static HttpResponse<byte[]> callUrl(String url) {
    return Unirest.get(url).asBytes();
  }

  private static void printResult(JsonResult result) throws Exception {
    System.out.println(mapper.writeValueAsString(result));
  }
}
