//g++ main.cpp -o myprogram -lmysqlcppconn

#include <iostream>
#include <stdexcept>
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/statement.h>
#include <cppconn/resultset.h>
#include <cppconn/exception.h>

int main() {
    try {
        sql::mysql::MySQL_Driver* driver;
        sql::Connection* con;
        sql::Statement* stmt;
        sql::ResultSet* res;

        // Connect to the MySQL database
        driver = sql::mysql::get_mysql_driver_instance();
        con = driver->connect("tcp://127.0.0.1:3306", "root", NULL); // Consider checking that the password can be NULL 

        // Connect to the specific database
        con->setSchema("hymns");

        stmt = con->createStatement();
        res = stmt->executeQuery("SELECT 'Hello World!' AS _message");

        while (res->next()) {
            std::cout << "Message: " << res->getString("_message") << std::endl;
        }

        delete res;
        delete stmt;
        delete con;
    }
    catch (sql::SQLException &e) {
        std::cerr << "SQL error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
