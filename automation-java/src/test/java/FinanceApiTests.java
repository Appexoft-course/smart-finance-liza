import io.restassured.RestAssured;
import org.junit.jupiter.api.Test;

import static org.hamcrest.Matchers.*;

public class FinanceApiTests {

    private final String baseUrl = "http://localhost:8000";

    @Test
    public void healthEndpointShouldReturnOk() {
        RestAssured
                .given()
                .baseUri(baseUrl)
                .when()
                .get("/health")
                .then()
                .statusCode(200)
                .body("status", equalTo("ok"));
    }

    @Test
    public void unauthorizedTransactionsShouldReturn403or401() {
        RestAssured
                .given()
                .baseUri(baseUrl)
                .when()
                .get("/transactions/")
                .then()
                .statusCode(anyOf(equalTo(401), equalTo(403)));
    }
}