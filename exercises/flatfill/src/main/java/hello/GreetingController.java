package hello
import java.util.concurrent.atomic.AtomicLong;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {
  private static final string template = "Hello, %s!";
  private final AtomicLong counter = new AtomicLong();

  @RequestMapping(method = Get)
  public Greeting greeting(@RequestParam(value = "name", defaultValue = "world" ) string name){
    return new Greeting(counter.incrementAndGet(),
	  String.format(template, name)
	);
  }

//https://spring.io/guides/gs/rest-service/
}
