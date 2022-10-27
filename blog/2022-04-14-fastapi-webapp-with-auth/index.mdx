---
title: How to create a FastAPI Web App with authentication
authors: sedwardes
draft: false
tags: [python, web, fastapi]
toc_min_heading_level: 2
toc_max_heading_level: 4
image: ./imgs/login.png
---

import CodeBlock from '@theme/CodeBlock';
import MainPy from '!!raw-loader!./main.py';
import RequirementsTxt from '!!raw-loader!./requirements.txt';
import IndexHtml from '!!raw-loader!./templates/index.html';
import LoginHtml from '!!raw-loader!./templates/login.html';
import PrivateHtml from '!!raw-loader!./templates/private.html';
import SiteMapHtml from '!!raw-loader!./templates/_site_map.html';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


I have recently been exploring how to use FastAPI to build web apps. Check out this recent blog post [How to create a FastAPI Web App with MongoDB and Beanie](../2022-03-18-fastapi-beanie-one-page/index.mdx). One area I have found difficult is configuring authentication for web apps in FastAPI. The FastAPI [security docs](https://fastapi.tiangolo.com/tutorial/security/) are really good, however they focus only on securing API endpoints, and not how to implement security for a web app. This blog post will demonstrate how to stand up a fully functional FastAPI web app with authentication.

<!--truncate-->

## TL/DR

All of the code can be found on GitHub: <https://github.com/SamEdwardes/personal-blog/tree/main/blog/2022-04-14-fastapi-webpage-with-auth>. You can download the code as a zip file using think link from [DownGit](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/SamEdwardes/personal-blog/tree/main/blog/2022-04-14-fastapi-webapp-with-auth). If you you want to see the complete code jump right to the [Full code overview](#full-code-overview) section of this blog post.

## Motivation

Setting up authentication is an important step in taking your app from a proof of concept to something you can actually deploy and use. In this blog post I want to implement authentication in a FastAPI app that works for **web apps**.

The site I will build is very simple, but hopefully it is complex enough to demonstrate how you could expand on these concepts and build out a full functional web app with authentication. There are two primary ways I want to use authentication:

1. Define endpoints that are only accessible to users who have authenticated, and
2. Have content in pages that will dynamically render only if a user is authenticated. 

<details>
<summary>
Expand this section to see a screenshot and brief description of each page.
</summary>

**Home page**

The home page has two different possible views. A view for users who are NOT logged in:

![home-page](./imgs/home-not-logged-in.png)

And a view for users who are logged in:

![home-page-auth](./imgs/home-logged-in.png)

**Login page**

A simple login page:

![login](./imgs/login.png)

**Private page**

A *"private"* page that can only be viewed by users who are logged in:

![private-logged-in](./imgs/private-page-logged-in.png)

If you try to view the page before logging in you will get this response:

![private-logged-in](./imgs/private-page-not-logged-in.png)

</details>

## Project setup

To get started first create a new directory for all of the project files and then create/activate a python virtual environment:

```bash
mkdir fastapi-webapp
cd fastapi-webapp
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel
```

Next, set up the file structure for the project:

```bash
touch main.py requirements.txt
mkdir templates
touch templates/_site_map.html templates/index.html templates/login.html templates/private.html
```

After running the commands your file structure should look like this:

```
.
├── main.py
├── requirements.txt
└── templates
   ├── _site_map.html
   ├── index.html
   ├── login.html
   └── private.html
```

Next, set up your *requirements.txt* file:

```bash
cat << EOF > requirements.txt
fastapi
uvicorn[standard]
python-multipart
fastapi-login
passlib[bcrypt]
python-jose
jinja2
rich
EOF
```

Install all of the requirements, and you are ready to go!

```
pip install -r requirements.txt
```

If you want to see the app running in action copy and paste the code from the [Full code overview](#full-code-overview) section into the appropriate file. Then run the following to launch the app:

```bash
uvicorn main:app --reload 
```

## Full code overview

Your project structure will look like this:

```
.
├── main.py
├── requirements.txt
└── templates
   ├── _site_map.html
   ├── index.html
   ├── login.html
   └── private.html
```

Below is the complete code for each file 🎉!

<Tabs>
    <TabItem value="requirements" label="requirements.txt">
        <CodeBlock title="requirements.txt">{RequirementsTxt}</CodeBlock>
    </TabItem>
    <TabItem value="main" label="main.py">
        <CodeBlock language="python" title="main.py">{MainPy}</CodeBlock>
    </TabItem>
    <TabItem value="index" label="index.html">
        <CodeBlock language="html" title="templates/index.html">{IndexHtml}</CodeBlock>
    </TabItem>
    <TabItem value="login" label="login.html">
        <CodeBlock language="html" title="templates/login.html">{LoginHtml}</CodeBlock>
    </TabItem>
    <TabItem value="private" label="private.html">
        <CodeBlock language="html" title="templates/private.html">{PrivateHtml}</CodeBlock>
    </TabItem>
    <TabItem value="sitemap" label="_site_map.html">
        <CodeBlock language="html" title="templates/_site_map.html">{SiteMapHtml}</CodeBlock>
    </TabItem>
</Tabs>

## Code walk through

In the following section I will walk through the key parts of code and describe what they are doing.

### Step 1: Models and data

In order to keep our example simple our app will not use an external database. Instead, we will just use [pydantic](https://pydantic-docs.helpmanual.io) models to define some dummy data. 

One key item it point out is the use of [passlib](https://passlib.readthedocs.io/en/stable/). When a we create our user we hash the password. Imagine that you were storing data about your users in a database. It is important to hash the password so that if data was ever exposed to the public the passwords  would be hashed, and not readable to the public.

We have also created a function called `get_user`. This function will be used in many places throughout to access users from our *"database"*.

```python
from typing import List
from pydantic import BaseModel
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

# --------------------------------------------------------------------------
# Models and Data
# --------------------------------------------------------------------------
class User(BaseModel):
    username: str
    hashed_password: str

# Create a "database" to hold your data. This is just for example purposes. In
# a real world scenario you would likely connect to a SQL or NoSQL database.
class DataBase(BaseModel):
    user: List[User]

DB = DataBase(
    user=[
        # highlight-start
        User(username="user1@gmail.com", hashed_password=crypto.hash("12345")),
        User(username="user2@gmail.com", hashed_password=crypto.hash("12345")),
        # highlight-end
    ]
)


# highlight-start
def get_user(username: str) -> User:
    user = [user for user in DB.user if user.username == username]
    if user:
        return user[0]
    return None
# highlight-end
```

Here is a quick example of what passlib hashed passwords look like:

```python
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
crypto.hash("12345")
# '$6$rounds=656000$r8Ft1VUrj3.ewIXT$HDtwFY1QPOh82U0H/pZOlqbEIk6RjMyL.Z5sc0ub1Yp9Fnkv9ZlZZ.bk/TGBThBfLnV2.KbvuC/CBMr/1rEP1.'
```

### Step 2: Setup FastAPI

Nothing too fancy is happening here. As with any FastAPI app we initiate our `FastAPI()` app object. I will point out a few areas of interest:

- `settings`: we create a settings object to store some settings information that will be accessed by different parts of our app. You do not need to do this using a class, but I chose to use a class as I think it is a clean way to organize the code.
- `templates`: To make a web app we need some way to build out a user interface. FastAPI comes with built in support for using [Jinja](https://palletsprojects.com/p/jinja/). The line `templates = Jinja2Templates(directory="templates")` tells FastAPI where our template files are located.

```python
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
# --------------------------------------------------------------------------
# Setup FastAPI
# --------------------------------------------------------------------------
class Settings:
    SECRET_KEY: str = "secret-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins
    COOKIE_NAME = "access_token"


app = FastAPI()
templates = Jinja2Templates(directory="templates")
settings = Settings()
```

### Step 3: Authentication logic

To me, this is the most complex part of the app. Expand the code snippet below to see all of the details. In this section I will walk through some of the key parts in more detail below.

<details>
<summary>
Expand to see the code snippets related to authentication 🔐
</summary>

```python
# --------------------------------------------------------------------------
# Authentication logic
# --------------------------------------------------------------------------
class OAuth2PasswordBearerWithCookie(OAuth2):
    """
    This class is taken directly from FastAPI:
    https://github.com/tiangolo/fastapi/blob/26f725d259c5dbe3654f221e608b14412c6b40da/fastapi/security/oauth2.py#L140-L171
    
    The only change made is that authentication is taken from a cookie
    instead of from the header!
    """
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )

    async def __call__(self, request: Request) -> Optional[str]:
        # IMPORTANT: this is the line that differs from FastAPI. Here we use 
        # `request.cookies.get(settings.COOKIE_NAME)` instead of 
        # `request.headers.get("Authorization")`
        authorization: str = request.cookies.get(settings.COOKIE_NAME) 
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="token")


def create_access_token(data: Dict) -> str:
    to_encode = data.copy()
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def get_user(username: str) -> User:
    user = [user for user in DB.user if user.username == username]
    if user:
        return user[0]
    return None


def authenticate_user(username: str, plain_password: str) -> User:
    user = get_user(username)
    if not user:
        return False
    if not crypto.verify(plain_password, user.hashed_password):
        return False
    return user


def decode_token(token: str) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Could not validate credentials"
    )
    token = token.removeprefix("Bearer").strip()
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError as e:
        print(e)
        raise credentials_exception
    
    user = get_user(username)
    return user


def get_current_user_from_token(token: str = Depends(oauth2_scheme)) -> User:
    """
    Get the current user from the cookies in a request.

    Use this function when you want to lock down a route so that only 
    authenticated users can see access the route.
    """
    user = decode_token(token)
    return user


def get_current_user_from_cookie(request: Request) -> User:
    """
    Get the current user from the cookies in a request.
    
    Use this function from inside other routes to get the current user. Good
    for views that should work for both logged in, and not logged in users.
    """
    token = request.cookies.get(settings.COOKIE_NAME)
    user = decode_token(token)
    return user
```

</details>

#### OAuth2PasswordBearer

FastAPI comes with a class out of the box named [`OAuth2PasswordBearer`](https://github.com/tiangolo/fastapi/blob/26f725d259c5dbe3654f221e608b14412c6b40da/fastapi/security/oauth2.py#L140-L171) (see FastAPI docs: [Security - First Steps](https://fastapi.tiangolo.com/tutorial/security/first-steps/?h=oauth2passwordbearer#fastapis-oauth2passwordbearer)). This is useful for authenticating APIs. However, I could not figure out how to use it in the context of a web app.

In order to use a similar approach that works with web apps I made a small modification to FastAPIs implementation of `OAuth2PasswordBearer`. Instead of getting the `authorization` from the `request` header, we get it from the `request` cookie.

<Tabs>
<TabItem value="passwordBearerMyApp" label="My implementation">
    

```python
class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )


    async def __call__(self, request: Request) -> Optional[str]:
        # highlight-start
        authorization: str = request.cookies.get(settings.COOKIE_NAME)
        # highlight-end
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param
```

</TabItem>
<TabItem value="passwordBearerFastAPI" label="FastAPI implementation">

```python
class OAuth2PasswordBearer(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )


    async def __call__(self, request: Request) -> Optional[str]:
        # highlight-start
        authorization: str = request.headers.get("Authorization")
        # highlight-end
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param
```

</TabItem>
</Tabs>

After defining our custom `OAuth2PasswordBearerWithCookie` we create an instance. 

```python
oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="token")
```

#### Access token

The access token is essentially how we will allow users to access protected web pages after authenticating. Just like in the FastAPI docs, I will use JWT tokens. Read more about them here: <https://jwt.io>. Our function `create_access_token` will be used to create a new JWT after a user has authenticated. The token will then be stored in the browser as a cookie (in a following code snippet).

```python
import datetime as dt
from jose import jwt

def create_access_token(data: Dict) -> str:
    to_encode = data.copy()
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt
```

#### Authenticating a user

We need a function that performs the actual user authentication when someone attempts to login. Our `authenticate_user` function will do two things:

1. First it will check to see if the username exists in the database.
2. If the username does exist, it will check to see that the passwords match. Since we have saved the hashed password in our database we need to hash the provided password using the same algorithm.

```python
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

def authenticate_user(username: str, plain_password: str) -> User:
    user = get_user(username)
    # highlight-start
    if not user:
        return False
    if not crypto.verify(plain_password, user.hashed_password):
        return False
    # highlight-end
    return user
```

#### Decoding the token

The above function `authenticate_user` is only called when a user first logs in. Our next function `decode_token` will be called to grant an already logged in user access to an endpoint. This function will decode the JWT so that we can get the required information from it. In our use cases, we need to decode the token so that we can figure out who the user is. There are a few key things to point out:

- We the line `token = token.removeprefix("Bearer").strip()` removes the string *"Bearer"* from the start of token string. This will be necessary when we are call `decode_token()` from within the `get_current_user_from_cookie()` function.

```python
from fastapi import HTTPException, status
from jose import JWTError, jwt

def decode_token(token: str) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Could not validate credentials"
    )
    # highlight-start
    token = token.removeprefix("Bearer").strip()
    # highlight-end
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError as e:
        print(e)
        raise credentials_exception
    
    user = get_user(username)
    return user
```

Below is a little example that demonstrates how JWT encodes your information. The username is actually stored in your cookie. But, since it is encrypted it is not possible to know the actual username unless your key the secret key to decrypt the token. 

```python
from jose import jwt

data = {"username": "sam", "admin": True}
encoded_jwt = jwt.encode(data, key="secret-key")
print(encoded_jwt)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbSIsImFkbWluIjp0cnVlfQ.gJbSlqbRTLm9LTCnvM9MMLDi2_Qqag1NM3m92oLZv9I
decoded_jwt = jwt.decode(encoded_jwt, key="secret-key")
print(decoded_jwt)
# {'username': 'sam', 'admin': True}
```

:::tip
You can see the cookies that are currently set in your browser using your browser's built in developer tools.
![screenshot](./imgs/cookie.png)
:::

#### Getting the user from JWT

In order to not ask the user for a username and password on every request we need a way to securely remember that they have already been validated. In section [Login for access token](#login-for-access-token) we will save our JWT token as a cookie. When decoded, that cookie contains the users username. If the token has a valid username, we will provide the user with access to the endpoint. To get a token, you need a username and password. So we can trust that if they have a token they have already authenticated.

The two functions below cover two different scenarios:

1. `get_current_user_from_token`: This function will be used when we want to protect an entire endpoint. For example see section [Private page](#private-page).
2. `get_current_user_from_cookie`: This function will be used for endpoints that will be available to uses who have authenticated and those who have not. However, the behavior will be different based on if they have authenticated or not. For example see section [Home page](#home-page)

```python
from fastapi import Request


def get_current_user_from_token(token: str = Depends(oauth2_scheme)) -> User:
    """
    Get the current user from the cookies in a request.

    Use this function when you want to lock down a route so that only 
    authenticated users can see access the route.
    """
    user = decode_token(token)
    return user


def get_current_user_from_cookie(request: Request) -> User:
    """
    Get the current user from the cookies in a request.
    
    Use this function from inside other routes to get the current user. Good
    for views that should work for both logged in, and not logged in users.
    """
    token = request.cookies.get(settings.COOKIE_NAME)
    user = decode_token(token)
    return user
```

#### Login for access token

OK, this is finally the last function related to authentication logic 🔒! In this function (which is also an API endpoint) we will save the JWT token in the users browser as a cookie. Note that this is the bit of code where we actually call `authenticate_user` to validate that the password is correct. This endpoint will be called when the user submits their username and password using the login page.

```python
@app.post("token")
def login_for_access_token(
    response: Response, 
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Dict[str, str]:
    # highlight-start
    user = authenticate_user(form_data.username, form_data.password)
    # highlight-end
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"username": user.username})
    
    # Set an HttpOnly cookie in the response. `httponly=True` prevents 
    # JavaScript from reading the cookie.
    # highlight-start
    response.set_cookie(
        key=settings.COOKIE_NAME, 
        value=f"Bearer {access_token}", 
        httponly=True
    )  
    # highlight-end
    return {settings.COOKIE_NAME: access_token, "token_type": "bearer"}
```

### Step 4: Views and HTML templates

If you made it this far, you are in the home stretch. All that is left is to define our views and HTML templates 🎉!

#### Home page

Our home page is actually pretty interesting. The content of the home page will be dynamic. If the user is logged in they will see one thing. If they are not logged in they will see something elses.

<Tabs>
<TabItem value="homeLoggedOut" label="Logged out">

> ![](./imgs/home-not-logged-in.png)

</TabItem>
<TabItem value="homeLoggedIn" label="Logged in">

> ![](./imgs/home-logged-in.png)

</TabItem>
</Tabs>

We achieve this in our API endpoint by attempting to get the current user from the cookie we set. If this function fails, it means the user is not logged in so we assign `None` to `user`.

<Tabs>
<TabItem value="homeEndPoint" label="endpoint">

```python
from fastapi.responses import HTMLResponse

# --------------------------------------------------------------------------
# Home Page
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    try:
        user = get_current_user_from_cookie(request)
    except:
        user = None
    context = {
        "user": user,
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)
```

</TabItem>
    <TabItem value="HomeView" label="view">
        <CodeBlock language="html" title="templates/index.html">{IndexHtml}</CodeBlock>
    </TabItem>
</Tabs>

Then on the templating side we render different content based on if `user` is `None` or not:


#### Private page

Our private page is only accessible to users who have logged in. Unlike our home page, we do not need any conditional logic here. 

<Tabs>
<TabItem value="privateLoggedOut" label="Logged out">

> ![](./imgs/private-page-not-logged-in.png)

</TabItem>
<TabItem value="privateLoggedIn" label="Logged in">

> ![](./imgs/private-page-logged-in.png)

</TabItem>
</Tabs>

How do we achieve this? They key is our use of `Depends` in the function definition. If we use `user: User = Depends(get_current_user_from_token))` on any endpoint, that endpoint will only be accessible to users who have logged in.

<Tabs>
<TabItem value="privateEndPoint" label="endpoint">

```python
from fastapi import Depends
from fastapi.responses import HTMLResponse

# --------------------------------------------------------------------------
# Private Page
# --------------------------------------------------------------------------
# A private page that only logged in users can access.
@app.get("/private", response_class=HTMLResponse)
# highlight-start
def index(request: Request, user: User = Depends(get_current_user_from_token)):
# highlight-end
    context = {
        "user": user,
        "request": request
    }
    return templates.TemplateResponse("private.html", context)
```

</TabItem>
    <TabItem value="privateView" label="view">
        <CodeBlock language="html" title="templates/private.html">{PrivateHtml}</CodeBlock>
    </TabItem>
</Tabs>

#### Login page - GET

Our login page is very simple. It is accessible to everyone, and there is no conditional logic. When you hit the "submit" button of the login form it will send a post request to `/auth/login`.

> ![](./imgs/login.png)

<Tabs>
<TabItem value="loginEndPoint" label="endpoint">

```python
from fastapi.responses import HTMLResponse

# --------------------------------------------------------------------------
# Login - GET
# --------------------------------------------------------------------------
@app.get("/auth/login", response_class=HTMLResponse)
def login_get(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("login.html", context)
```

</TabItem>
    <TabItem value="loginView" label="view">
        <CodeBlock language="html" title="templates/login.html">{LoginHtml}</CodeBlock>
    </TabItem>
</Tabs>

#### Login page - POST

The "post" side of logging in is a bit more complicated. There are a few things happening here:

- We create a class `LoginForm` to handle the logic of validating the form data. In the event that the submitted form data is not valid we will re-render the *"templates/login.html"* with the same form data and an error message.
- In the event that the form is valid, we will attempt to validate the users credentials. The line `login_for_access_token(response=response, form_data=form)` will attempt to log the user in, and if successful set a cookie with the users data encoded.
- Notice that we we validate the form our response is `response = RedirectResponse("/", status.HTTP_302_FOUND)`. This will redirect our user to the home page. It is important that you include `status.HTTP_302_FOUND`. If you do not, FastAPI will send a post request against `"/"`. We have not defined a post request endpoint for `"/"`. By using `status.HTTP_302_FOUND` FastAPI knows to send a get request (this part was tricky and took me a lot of googling to figure out 🕵️). 

<Tabs>
<TabItem value="loginEndPoint" label="endpoint">

```python
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

# --------------------------------------------------------------------------
# Login - POST
# --------------------------------------------------------------------------
class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        if not self.errors:
            return True
        return False


@app.post("/auth/login", response_class=HTMLResponse)
async def login_post(request: Request):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            response = RedirectResponse("/", status.HTTP_302_FOUND)
            login_for_access_token(response=response, form_data=form)
            form.__dict__.update(msg="Login Successful!")
            console.log("[green]Login successful!!!!")
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("login.html", form.__dict__)
    return templates.TemplateResponse("login.html", form.__dict__)
```

</TabItem>
    <TabItem value="loginView" label="view">
        <CodeBlock language="html" title="templates/login.html">{LoginHtml}</CodeBlock>
    </TabItem>
</Tabs>

#### Logout endpoint

The final feature our web app is the ability to logout. There is no logout view, instead we only have a logout endpoint. In the site map we include a link to call the logout endpoint. The logic of logging out is pretty simple:

1. Delete the cookie containing the encoded user information.
2. Redirect the user to the home page.

<Tabs>
<TabItem value="logoutEndPoint" label="endpoint">

```python
from fastapi.responses import HTMLResponse, RedirectResponse

# --------------------------------------------------------------------------
# Logout
# --------------------------------------------------------------------------
@app.get("/auth/logout", response_class=HTMLResponse)
def login_get():
    response = RedirectResponse(url="/")
    response.delete_cookie(settings.COOKIE_NAME)
    return response
```

</TabItem>
    <TabItem value="siteMapView" label="site map view">
        <CodeBlock language="html" title="templates/_site_map.html">{SiteMapHtml}</CodeBlock>
    </TabItem>
</Tabs>

## Wrap up

Congratulations 🎉! Your web app is complete and ready to go. Check out the complete source code on GitHub: <https://github.com/SamEdwardes/personal-blog/tree/main/blog/2022-04-14-fastapi-webapp-with-auth>. If you have any questions or feedback find me on twitter [@TheReaLSamlam](https://twitter.com/TheReaLSamlam), or submit an issue on GitHub: <https://github.com/SamEdwardes/personal-blog/issues/new/choose>.

## Reference

Here are some of the resources I found useful while researching this blog post:

- <https://fastapi.tiangolo.com/tutorial/security/>
- <https://www.fastapitutorial.com/blog/authentication-in-fastapi/>
- <https://github.com/talkpython/web-applications-with-fastapi-course>
- <https://stackoverflow.com/questions/62119138/how-to-do-a-post-redirect-get-prg-in-fastapi>
- <https://github.com/MushroomMaula/fastapi_login>
- <https://github.com/mjhea0/awesome-fastapi>
- <https://kernelpanic.io/demystifying-authentication-with-fastapi-and-a-frontend>
- <https://github.com/nofoobar/JobBoard-Fastapi/tree/0e1bdf676a66e3f341d00c590b3fd07b269488f4>