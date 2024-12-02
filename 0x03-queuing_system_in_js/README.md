# 0x03. Queuing System in JS

`Backend` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

---

![meme](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/1486e02a78cdf7b4557c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20241202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241202T152417Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=766aeb22706bb4c5e11e04f36ff08c2c8788a114f8fa5fc508129b08d3d53a08)

---

## Resources
#### Read or watch:

- [Redis quick start](https://redis.io/docs/getting-started/)
- [Redis client interface](https://redis.io/docs/ui/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue](https://github.com/Automattic/kue) _deprecated but still in use in the industry_

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) **without the help of Google**:
- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements

- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A `README.md` file, at the root of the project, is mandatory
- Your code should use the `js` extension

## Required Files for the Project

### `package.json`

<details>
<summary>Click to show/hide file contents</summary>
<pre>

{
  "name": "queuing_system_in_js",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/.bin/mocha --require @babel/register --exit",
    "dev": "nodemon --exec babel-node --presets @babel/preset-env"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1",
    "kue": "^0.11.6",
    "redis": "^2.8.0"
  },
  "devDependencies": {
    "@babel/cli": "^7.8.0",
    "@babel/core": "^7.8.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.8.2",
    "@babel/register": "^7.8.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "nodemon": "^2.0.2",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}

</pre>
</details>

### `.babelrc`

<details>
<summary>Click to show/hide file contents</summary>
<pre>

{
  "presets": [
    "@babel/preset-env"
  ]
}

</pre>
</details>


### and...
Don't forget to run `$ npm install` when you have the `package.json`
