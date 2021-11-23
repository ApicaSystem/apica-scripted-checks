using System.Text.Json.Serialization;
public class Result
{
    [JsonPropertyName("returncode")]
    public int ReturnCode { get; set; }

    [JsonPropertyName("stdout")]
    public string Stdout { get; set; }

    [JsonPropertyName("stderr")]
    public string Stderr { get; set; }

    [JsonPropertyName("message")]
    public string Message { get; set; }

    [JsonPropertyName("start_timestamp_ms")]
    public long StartTimeMs { get; set; }

    [JsonPropertyName("end_timestamp_ms")]
    public long EndTimeMs { get; set; }

    [JsonPropertyName("value")]
    public string Value { get; set; }

    public bool DotNet { get; set; }
}
