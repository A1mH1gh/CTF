
# Try
```
SELECT * FROM user WHERE uid=''||';
SELECT * FROM user WHERE uid='1'like'a';


'%20%75nion%20%73elect%201# =>' union select 1#
'%20%55nion(%53elect%201,2,3,4,5,6)#


```
### 컬럼 갯수 알아내기
```

```


# 공백이 필터링된 경우에도 SQL 인젝션을 시도할 수 있는 여러 가지 우회 방법

공백이 필터링된 경우에도 SQL 인젝션을 시도할 수 있는 여러 가지 우회 방법이 있습니다. SQL은 다양한 형태의 공백 대체 문자를 허용하며, 이를 통해 필터링을 우회할 수 있습니다. 몇 가지 대표적인 우회 방법은 다음과 같습니다.

### 1. **주석을 사용하는 방법 (`/**/`)**
   SQL에서는 공백 대신 주석을 사용할 수 있습니다. `/*`와 `*/` 사이의 내용은 SQL에서 주석 처리되므로, 이를 공백 대신 사용할 수 있습니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin'/**/OR/**/1;
   ```

   여기서 `/**/`는 공백처럼 작동합니다.

### 2. **URL 인코딩을 사용하는 방법**
   일부 경우에는 SQL 문을 URL 인코딩하여 공백을 필터링하는 방식을 우회할 수 있습니다. URL 인코딩에서 공백은 `%20`으로 표현됩니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin'%20OR%201;
   ```

   하지만, URL 인코딩이 자동으로 해석되지 않는 환경에서는 이 방식이 작동하지 않을 수 있습니다.

### 3. **탭이나 새 줄 문자 사용**
   SQL 구문에서 공백 대신 탭 문자(`\t`)나 새 줄 문자(`\n`)를 사용할 수 있습니다. 일부 필터링 시스템은 이러한 문자를 무시할 수 있으므로 이를 이용하여 공백을 대체할 수 있습니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin'\tOR\t1;
   ```

   혹은

   ```sql
   SELECT * FROM table_name WHERE id='admin'\nOR\n1;
   ```

### 4. **데이터베이스 함수 활용**
   SQL 함수 또는 연산자를 사용하여 `OR` 구문을 대체할 수 있습니다. 예를 들어, 문자열 결합 함수를 이용하여 키워드를 구성할 수 있습니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin' || 1=1;
   ```

   일부 데이터베이스에서는 문자열 결합 연산자 `||`로 논리 연산자 `OR`를 대체할 수 있습니다. 이는 주로 특정 DBMS(예: PostgreSQL)에서 사용됩니다.

### 5. **`UNION`을 활용한 우회**
   공백 없이 `OR`을 사용할 수 없는 상황에서는 `UNION`을 이용하여 여러 쿼리의 결과를 결합하는 방식으로 데이터를 노출시킬 수 있습니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin' UNION SELECT 1,2,3;
   ```

### 6. **대체 문자 인코딩 또는 이스케이프 사용**
   일부 환경에서는 문자 인코딩이나 이스케이프 문자를 사용하여 공백을 우회할 수 있습니다. 예를 들어, 공백을 ASCII 또는 다른 인코딩 방식으로 표현할 수 있습니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin'%0bOR%0b1;
   ```

   여기서 `%0b`는 ASCII 탭 문자로, 일부 필터링 시스템에서 공백과 동일하게 처리될 수 있습니다.

### 7. **연산자 우회**
   `OR` 연산자 대신 논리 연산의 다른 표현을 사용할 수 있습니다. 예를 들어, `OR`과 동일한 동작을 하는 연산자가 있으면 이를 사용할 수 있습니다.

   ```sql
   SELECT * FROM table_name WHERE id='admin'|1=1;
   ```

   일부 데이터베이스에서는 `|`가 비트 OR 연산자이지만, 논리적으로도 사용할 수 있습니다.

### 결론:
공백 필터링을 우회하기 위한 방법은 다양하며, 각 방법은 사용하는 데이터베이스 시스템과 필터링 메커니즘에 따라 달라질 수 있습니다. SQL 인젝션을 방지하려면 이러한 우회 기법을 방지할 수 있는 **Prepared Statements(준비된 구문)** 또는 **ORM(Object-Relational Mapping)**을 사용하고, 사용자 입력을 철저히 검증하는 것이 중요합니다.


# Like
SQL 인젝션에서 **`LIKE`** 연산자는 주로 문자열 검색에 사용되며, 공격자가 이를 악용하여 쿼리의 결과를 조작할 수 있습니다. SQL 인젝션은 공격자가 데이터베이스 쿼리를 조작하여 악의적인 코드를 실행하게 하는 보안 취약점인데, `LIKE`는 이 과정에서 문자열 패턴 매칭을 이용한 공격에 사용될 수 있습니다.

### 예시
`LIKE`는 SQL에서 특정 패턴과 일치하는지 확인할 때 사용됩니다. 일반적인 쿼리는 다음과 같습니다:

```sql
SELECT * FROM users WHERE username LIKE 'admin%';
```

이 쿼리는 "admin"으로 시작하는 모든 username을 찾습니다. 그러나, 만약 입력 값이 적절하게 검증되지 않는다면 공격자가 쿼리를 변형할 수 있습니다.

#### SQL 인젝션 예시:
```sql
SELECT * FROM users WHERE username LIKE '%a%' OR '1'='1';
```

이러한 인젝션은 항상 참이 되는 조건을 포함시켜, 데이터베이스에서 모든 사용자 정보를 반환하게 만들 수 있습니다. 공격자는 와일드카드(`%`), 밑줄(`_`) 등을 사용해 더 복잡한 검색 패턴을 만들고 데이터베이스 시스템을 악용할 수 있습니다.

#### 방어 방법:
1. **Prepared Statements(준비된 쿼리)**: SQL 인젝션 공격을 방어하는 가장 좋은 방법 중 하나는 미리 컴파일된 쿼리를 사용하는 것입니다.
   
2. **Input Validation(입력 값 검증)**: 사용자의 입력 값을 엄격하게 검증하여, 악의적인 패턴을 차단합니다.

3. **ORM(객체 관계 매핑) 사용**: ORM을 사용하면 SQL을 직접 작성하지 않아도 되기 때문에 SQL 인젝션 위험을 줄일 수 있습니다.

`LIKE`를 사용할 때도 반드시 이러한 방어 방법을 고려해야만 인젝션 공격에 대한 위험을 최소화할 수 있습니다.