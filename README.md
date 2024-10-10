# CTF

# PHP 구동하기
```
\CTF\Dreamhack\php-8.3.12-nts-Win32-vs16-x86
```

Visual Studio에서 PHP 서버를 구동하려면 **PHP 개발 환경**과 **내장 웹 서버** 또는 **로컬 웹 서버**(예: Apache) 설정이 필요합니다. 여기서는 Visual Studio를 통해 PHP 서버를 구동하는 방법을 단계별로 설명합니다.

### 1. **PHP 설치**
   - [PHP 공식 웹사이트](https://www.php.net/downloads)에서 최신 PHP 버전을 다운로드합니다.
   - 다운로드한 PHP 압축 파일을 원하는 디렉토리에 풀고, **경로를 환경 변수에 추가**합니다.
     - Windows에서 경로 추가: `시스템 속성 > 고급 시스템 설정 > 환경 변수 > PATH`

### 2. **PHP 서버 실행 확인**
   - 터미널 또는 명령 프롬프트에서 다음 명령어로 PHP가 제대로 설치되었는지 확인합니다.

     ```bash
     php -v
     ```

   - PHP 버전 정보가 출력되면 정상적으로 설치된 것입니다.

### 3. **Visual Studio에 PHP 파일 추가**
   - Visual Studio에서 PHP 파일을 생성하고 코드를 작성합니다.
   - 예: `index.php`

### 4. **Visual Studio에서 PHP 서버 실행하기**
   PHP 내장 서버를 사용하여 PHP 파일을 실행할 수 있습니다. Visual Studio의 터미널 또는 명령 프롬프트에서 다음 명령을 사용하세요.

   ```bash
   php -S localhost:8000
   ```

   - 이 명령은 PHP 내장 서버를 사용하여 `localhost`의 `8000` 포트에서 서버를 실행합니다.
   - `index.php` 파일이 프로젝트 루트에 있어야 하며, 다른 폴더에 있는 경우 해당 경로로 이동한 후 위 명령을 실행해야 합니다.

### 5. **브라우저에서 확인하기**
   - 브라우저에서 `http://localhost:8000`으로 이동하여 서버가 정상적으로 작동하는지 확인합니다.

### 6. **추가 옵션: XAMPP 또는 WAMP와 연동**
   - PHP 내장 서버 대신 XAMPP 또는 WAMP와 같은 로컬 서버를 사용하여 PHP 코드를 구동할 수도 있습니다.
   - PHP 파일을 XAMPP의 `htdocs` 디렉토리에 넣고 `http://localhost/{파일명}.php`로 접근하면 됩니다.

### 요약
- PHP 설치 및 환경 변수 추가
- Visual Studio에서 PHP 파일 작성
- 터미널에서 `php -S localhost:8000` 명령으로 PHP 내장 서버 구동
- 브라우저에서 `localhost:8000`으로 확인

이 과정을 통해 Visual Studio에서 PHP 서버를 간단히 구동할 수 있습니다.