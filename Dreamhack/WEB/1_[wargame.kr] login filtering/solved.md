```C++
if (isset($_POST['id']) && isset($_POST['ps'])) {
    include("./lib.php");
    #include for $FLAG,
    $DB_username,
    $DB_password.

    $conn = mysqli_connect("localhost", $DB_username, $DB_password, "login_filtering");
    mysqli_query($conn, "set names utf8");

    $id = mysqli_real_escape_string($conn, trim($_POST['id']));
    $ps = mysqli_real_escape_string($conn, trim($_POST['ps']));

    $row = mysqli_fetch_array(mysqli_query($conn, "select * from user where id='$id' and ps=md5('$ps')"));
    if (isset($row['id'])) {
        if ($id == 'guest' || $id == 'blueh4g') {
            echo "your account is blocked";
        } else {
            echo "login ok"."<br />";
            echo "FLAG : ".$FLAG;
        }
    }
}
```

### 대문자/소문자 처리 방식을 악용
select * from user where id='Guest' pw ='9999';
```
Success
+-------+------+
|  id   |  pw  |
+-------+------+
| guest | 9999 |
+-------+------+
```

### 참고
SQL 쿼리에서 **대소문자 식별 여부**는 **데이터베이스 시스템**과 **문자열 비교 시 사용하는 설정**에 따라 다릅니다.

### 1. **MySQL과 MariaDB**

- **기본 설정**: MySQL과 MariaDB에서는 **대소문자를 구분하지 않는(collation 설정이 `ci`로 끝나는) 비교 방식**이 기본입니다. 예를 들어 `WHERE name = 'Alice'`와 `WHERE name = 'alice'`는 동일하게 취급됩니다.
- **대소문자 구분 설정**: 대소문자를 구분하고 싶다면, **`BINARY`** 키워드를 사용하거나 대소문자 구분(collation이 `cs`로 끝나는)으로 설정할 수 있습니다.

    ```sql
    SELECT * FROM users WHERE BINARY name = 'Alice';
    ```

    또는, 테이블이나 열에 대해 대소문자 구분 설정을 명시할 수 있습니다:

    ```sql
    CREATE TABLE users (
      name VARCHAR(100) COLLATE utf8mb4_bin
    );
    ```

### 2. **PostgreSQL**

- PostgreSQL은 기본적으로 **대소문자를 구분**합니다. 즉, `WHERE name = 'Alice'`와 `WHERE name = 'alice'`는 서로 다르게 인식됩니다.
- 대소문자를 구분하지 않고 비교하려면 `ILIKE` 키워드를 사용하거나, 문자열을 소문자로 변환하는 함수인 `LOWER()`를 사용하여 비교할 수 있습니다.

    ```sql
    SELECT * FROM users WHERE name ILIKE 'alice';
    -- 또는
    SELECT * FROM users WHERE LOWER(name) = LOWER('Alice');
    ```

### 3. **SQL Server (MSSQL)**

- SQL Server는 **대소문자 구분 여부**가 데이터베이스 또는 열의 **Collation 설정**에 따라 달라집니다.
- 기본적으로는 **대소문자를 구분하지 않지만**, 필요에 따라 `COLLATE` 절을 사용하여 대소문자 구분을 강제할 수 있습니다.

    ```sql
    SELECT * FROM users WHERE name = 'Alice' COLLATE Latin1_General_CS_AS;
    ```

### 요약

- **MySQL/MariaDB**: 기본적으로 대소문자를 구분하지 않지만 설정으로 변경 가능.
- **PostgreSQL**: 기본적으로 대소문자를 구분하지만, `ILIKE` 등을 사용하여 구분하지 않도록 설정 가능.
- **SQL Server**: Collation 설정에 따라 달라지며, 설정을 통해 구분 여부를 조정할 수 있음.

대소문자 구분은 **데이터베이스 설정**과 **쿼리 옵션**에 따라 조정할 수 있으므로, 대소문자 구분이 필요한 경우 이를 명시적으로 처리하는 것이 좋습니다.

