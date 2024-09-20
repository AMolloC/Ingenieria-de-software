// UserRepository.java
package com.sis324.ecomerce.repositories;
import org.springframework.data.jpa.repository.JpaRepository;
import com.sis324.ecomerce.models.User;

public interface UserRepository extends JpaRepository<User, Long> {
}



/* application.properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true

*/

