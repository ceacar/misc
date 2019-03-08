import org.junit.Test;
import static org.junit.Assert.*;
import com.ceacar.ClockAngel;

public class FailingTest {
   @Test
   public void testThatSucceed() {
	   ClockAngel ca = new ClockAngel();
	   assertTrue("clock angle 180", ca.getAngel(12, 30) == 180);
   }

   @Test
   public void testThatFails() {
       assertTrue("This should fail", false);
   }

}
