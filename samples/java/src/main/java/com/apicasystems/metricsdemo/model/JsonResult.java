package com.apicasystems.metricsdemo.model;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import lombok.Data;

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class JsonResult {
  @JsonProperty("returncode")
  private Long returncode;

  @JsonProperty("stdout")
  private String stdout;

  @JsonProperty("start_time")
  private double startTime;

  @JsonProperty("cmd")
  private List<String> cmd = new LinkedList<>();

  @JsonProperty("value")
  private String value;

  @JsonProperty("end_time")
  private double endTime;

  @JsonProperty("stderr")
  private String stderr;

  @JsonProperty("message")
  private String message;

  @JsonProperty("unit")
  private String unit;

  @JsonProperty("version")
  private String version;

  @JsonIgnore
  private Map<String, Object> additionalProperties = new HashMap<>();

  @JsonAnyGetter
  public Map<String, Object> getAdditionalProperties() {
    return this.additionalProperties;
  }

  @JsonAnySetter
  public void setAdditionalProperty(String name, Object value) {
    this.additionalProperties.put(name, value);
  }
}
