using System;
using System.Text.Json;

namespace dnet
{
    class Program
    {
        static void Main(string[] args)
        {

            long x = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds();
            var result = new Result 
            {
                ReturnCode = 0,
                Stdout = "stdout",
                Stderr = "err",
                Message = "Message from dotnet.",
                StartTimeMs = x,
                EndTimeMs = x + 100,
                Value = "100",
                DotNet = true
            };

            string jsonString = JsonSerializer.Serialize(result);

            Console.WriteLine(jsonString);
        }
    }
}
