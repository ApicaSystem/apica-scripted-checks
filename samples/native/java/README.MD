# Scripted Checks Example Java Project

You may reuse the src/main/java/com/apicasystems/metricsdemo/model/JsonResult class for easy integration into your own projects (check pom.xml for dependencies).


## I Want To Run the Sample
Build the example executable jar by running

```bash
mvn clean package
```

You may then test your jar by running

```bash
java -jar ./demo-metrics-jar-with-dependencies.jar
```

Or just download the demo-driver.jar file.

## How does the provided jar run in our environment
The jar you provide is run by the Java 11 JRE and runs on the CLI, your provided jar should contain all dependencies. Your jar should only print out the result JSON that is expected.
