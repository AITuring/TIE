数组是最常见的数据结构，在不同的语言中，数组有着不同的方法。下面详细阐述js数组的方法：

### 数组中的元素类型
数组中可以存放任意类型的数据，例如字符串、数字、布尔值、对象等。
比如：
```js
var arr = ['qianguyihao', 28, true, {name: 'qianguyihao'}];
```

### 创建一个数组
1. 最简单的方式，也是最常用的：

```javascript
var a = [1,2,3];
```
2. 利用关键词`new`，通过构造函数创建数组

```javascript
var arr2 = new Array(); // 参数为空
    var arr3 = new Array(4); // 参数为一个数值
    var arr4 = new Array(15, 16, 17); // 参数为多个数值

    console.log(typeof arr1);  // 打印结果：object

    console.log("arr1 = " + JSON.stringify(arr1));
    console.log("arr2 = " + JSON.stringify(arr2));
    console.log("arr3 = " + JSON.stringify(arr3));
    console.log("arr4 = " + JSON.stringify(arr4));
```
打印的结果：
```js
 object

arr1 = [11,12,13]
arr2 = []
arr3 = [null,null,null,null]
arr4 = [15,16,17]
```
3. 实际上`new Array === Array`，加不加`new`，没有任何影响

```javascript
var a = Array(1,2,3); // a=[1,2,3]
```

### 数组的基本操作

#### 数组的索引

**索引** (下标) ：用来访问数组元素的序号，代表的是数组中的元素在数组中的位置（下标从 0 开始算起）。

数组可以通过索引来访问、设置、修改对应的数组元素。

#### 向数组中添加元素
语法：
```
数组[索引] = 值
```
代码举例：

```js
var arr = [];

// 向数组中添加元素
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
arr[3] = 40;
arr[5] = 50;

console.log(JSON.stringify(arr));
```
打印结果：
```
[10,20,30,40,null,50]
```
#### 获取数组中的元素
语法：
```
数组[索引]
```

**注意**：如果读取不存在的索引（比如元素没那么多），系统不会报错，而是返回undefined。

代码举例：
```js
var arr = [21, 22, 23];
console.log(arr[0]); // 打印结果：21
console.log(arr[5]); // 打印结果：undefined
```    
#### 获取数组的长度

可以使用length属性来获取数组的长度(即“元素的个数”)。

数组的长度是元素个数，不要跟索引号混淆。

语法：
```
数组的长度 = 数组名.length;
```
代码举例：
```js
var arr = [21, 22, 23];
console.log(arr.length); // 打印结果：3
```

#### 修改数组长度

- 如果修改的length大于原长度，则多出部分会空出来，置为 null。
- 如果修改的length小于原长度，则多出的元素会被删除，数组将从后面删除元素。

代码举例：
```js
var arr1 = [11, 12, 13];
var arr2 = [21, 22, 23];

// 修改数组 arr1 的 length
arr1.length = 1;
console.log(JSON.stringify(arr1));

// 修改数组 arr2 的 length
arr2.length = 5;
console.log(JSON.stringify(arr2));
```
打印结果：
```js
[11]
[21,22,23,null,null]
```
#### 遍历数组

最简单的做法是通过 for 循环，遍历数组中的每一项。举例：

```js
var arr = [10, 20, 30, 40, 50];

for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]); // 打印出数组中的每一项
    }
```

### 数组的常见方法

#### 四个基本方法(添加，删除元素)

##### push()

push()：向数组的**最后面**插入**一个或多个元素**，**返回结果为该数组新的长度**。

语法：
```
数组的新长度 = 数组.push(元素);
```
代码举例：
```javascript
var arr = [1,2,3];

var result1 = arr.push(4); // 末尾插入一个元素
var result2 = arr.push(5,6); // 末尾插入多个元素

console.log(result1); // 4
console.log(result2); // 6
console.log(JSON.stringify(arr)); // [1,2,3,4,5,6]
```
##### pop()

pop()：删除数组中的**最后一个**元素，返回结果为**被删除的元素**。

语法：
```
被删除的元素 = 数组.pop();

代码举例：
```js
var arr = [1,2,3,4];
var result1 = arr.pop();
console.log(result1); // 4
console.log(JSON.stringify(arr)); // [1,2,3]
```

##### unshift()

unshift()：在数组**最前面**插入**一个或多个元素**，返回结果为该数组**新的长度**。插入元素后，**其他元素的索引会依次调整**。

语法：
```
数组的新长度 = 数组.unshift(元素);
```
代码举例：

```js
var arr = [1,2,3];

var result1 = arr.unshift(4); // 最前面插入一个元素
var result2 = arr.unshift(5,6); // 最前面插入多个元素

console.log(result1); // 4
console.log(result2); // 6
console.log(JSON.stringify(arr)); // [5,6,4,1,2,3]
```

##### shift()

shift()：删除数组中的**第一个元素**，返回结果为**被删除的元素**。

语法：
```
被删除的元素 = 数组.shift();
```
代码举例：
```js
var arr = [1,2,3];

var result1 = arr.shift();

console.log(result1); // 1
console.log(JSON.stringify(arr)); // [2,3]
```
#### 数组的其他常见方法

##### slice()

slice()：从数组中**提取**指定的**一个或者多个元素**，返回结果为**新的数组**（**不会改变原来的数组**）。

**备注**：该方法不会改变原数组，而是将截取到的元素封装到一个新数组中返回。

语法：
```
新数组 = 原数组.slice(开始位置的索引, 结束位置的索引);    //注意：包含开始索引，不包含结束索引
```

举例：
```js
var arr = ["a", "b", "c", "d", "e", "f"];

var result1 = arr.slice(2); //从第二个值开始提取
var result2 = arr.slice(-2); //提取最后两个元素
var result3 = arr.slice(2, 4); //提取从第二个到第四个之间的值（不包括第四个值）
var result4 = arr.slice(4, 2); //空

console.log("arr:" + JSON.stringify(arr));
console.log("result1:" + JSON.stringify(result1));
console.log("result2:" + JSON.stringify(result2));
console.log("result3:" + JSON.stringify(result3));
console.log("result4:" + JSON.stringify(result4));
```
打印结果：
```
arr:["a","b","c","d","e","f"]
result1:["c","d","e","f"]
result2:["e","f"]
result3:["c","d"]
result4:[]
```

**补充**：

很多前端开发人员会用 slice()将伪数组，转化为真数组。写法如下：
```js
array = Array.prototye.slice.call(arrayLike)
```
或者
```js
array = [].slice.call(arrayLike)
```
ES6 看不下去这种蹩脚的转化方法，于是出了一个新的 API：（专门用来将伪数组转化成真数组）
```js
array = Array.from(arrayLike)
```

##### splice()

splice()：从数组中**删除**指定的**一个或多个元素**，返回结果为**新的数组**（会**改变原来的数组**）。

备注：该方法会改变原数组，会**将指定元素从原数组中删除**；**被删除的元素会封装到一个新的数组**中返回。

语法：
```
新数组 = 原数组.splice(起始索引index, 需要删除的个数, 第三个参数, 第四个参数...);
```
上方语法中，第三个及之后的参数，表示：向原数组中添加新的元素，这些元素将会自动插入到开始位置索引的前面。

举例1：

    var arr1 = ["a", "b", "c", "d", "e", "f"];
    var result1 = arr1.splice(1); //从第index为1的位置开始，删除元素

    console.log("arr1：" + JSON.stringify(arr1));
    console.log("result1：" + JSON.stringify(result1));
打印结果：

    arr1：["a"]
    result1：["b","c","d","e","f"]
举例2：

    var arr2 = ["a", "b", "c", "d", "e", "f"];
    var result2 = arr2.splice(-2); //删除最后两个元素

    console.log("arr2：" + JSON.stringify(arr2));
    console.log("result2：" + JSON.stringify(result2));
打印结果：

    arr2：["a","b","c","d"]
    result2：["e","f"]
举例3：

    var arr3 = ["a", "b", "c", "d", "e", "f"];
    var result3 = arr3.splice(1, 3); //从第index为1的位置开始删除元素,一共删除三个元素

    console.log("arr3：" + JSON.stringify(arr3));
    console.log("result3：" + JSON.stringify(result3));
打印结果：

    arr3：["a","e","f"]
    result3：["b","c","d"]
举例4：（我们来看看第三个参数的用法）

var arr4 = ["a", "b", "c", "d", "e", "f"];

//从第index为1的位置开始删除元素,一共删除三个元素。并且在 index=1 的前面追加两个元素
var result4 = arr4.splice(1, 3, "千古壹号", "vae");

console.log("arr4：" + JSON.stringify(arr4));
console.log("result4：" + JSON.stringify(result4));
打印结果：

arr4：["a","千古壹号","vae","e","f"]
result4：["b","c","d"]
concat()
concat()：连接两个或多个数组，返回结果为新的数组。（不会改变原数组）

语法：

    新数组 = 数组1.concat(数组2, 数组3 ...);
举例：

    var arr1 = [1, 2, 3];
    var arr2 = ["a", "b", "c"];
    var arr3 = ["千古壹号", "vae"];

    var result1 = arr1.concat(arr2);

    var result2 = arr2.concat(arr1, arr3);

    console.log("arr1 =" + JSON.stringify(arr1));
    console.log("arr2 =" + JSON.stringify(arr2));
    console.log("arr3 =" + JSON.stringify(arr3));

    console.log("result1 =" + JSON.stringify(result1));
    console.log("result2 =" + JSON.stringify(result2));
打印结果：

arr1 =[1,2,3]
arr2 =["a","b","c"]
arr3 =["千古壹号","vae"]

result1 =[1,2,3,"a","b","c"]
result2 =["a","b","c",1,2,3,"千古壹号","vae"]
从打印结果中可以看到，原数组并没有被修改。

join()
join()：将数组转换为字符串，返回结果为转换后的字符串（不会改变原来的数组）。

补充：join()方法可以指定一个字符串作为参数，这个字符串将会成为数组中元素的连接符；如果不指定连接符，则默认使用 , 作为连接符，此时和 toString()的效果是一致的。

语法：

    新的字符串 = 原数组.join(参数); // 参数选填
代码举例：

    var arr = ["a", "b", "c"];

    var result1 = arr.join(); // 这里没有指定连接符，所以默认使用 , 作为连接符

    var result2 = arr.join("-"); // 使用指定的字符串作为连接符

    console.log(typeof arr); // 打印结果：object
    console.log(typeof result1); // 打印结果：string

    console.log("arr =" + JSON.stringify(arr));
    console.log("result1 =" + JSON.stringify(result1));
    console.log("result2 =" + JSON.stringify(result2));
上方代码中，最后三行的打印结果是：

arr =["a","b","c"]
result1 =a,b,c
result2 =a-b-c
reverse()
reverse()：反转数组，返回结果为反转后的数组（会改变原来的数组）。

语法：

    反转后的数组  =  数组.reverse();
举例：

    var arr = ["a", "b", "c", "d", "e", "f"];

    var result = arr.reverse(); // 将数组 arr 进行反转

    console.log("arr =" + JSON.stringify(arr));
    console.log("result =" + JSON.stringify(result));
打印结果：

arr =["f","e","d","c","b","a"]
result =["f","e","d","c","b","a"]
从打印结果可以看出，原来的数组已经被改变了。

sort()方法
sort()方法要好好理解。所以，我们单独用一大段来讲。

sort()：对数组的元素进行从小到大来排序（会改变原来的数组）。

sort()方法举例：无参时
如果在使用 sort() 方法时不带参，则默认按照Unicode编码，从小到大进行排序。

举例1：（当数组中的元素为字符串时）

    var arr1 = ["e", "b", "d", "a", "f", "c"];

    var result = arr1.sort(); // 将数组 arr1 进行排序

    console.log("arr1 =" + JSON.stringify(arr1));
    console.log("result =" + JSON.stringify(result));
打印结果：

    arr1 =["a","b","c","d","e","f"]
    result =["a","b","c","d","e","f"]
从上方的打印结果中，我们可以看到，sort方法会改变原数组，而且方法的返回值也是同样的结果。

举例2：（当数组中的元素为数字时）

    var arr2 = [5, 2, 11, 3, 4, 1];

    var result = arr2.sort(); // 将数组 arr2 进行排序

    console.log("arr2 =" + JSON.stringify(arr2));
    console.log("result =" + JSON.stringify(result));
打印结果：

    arr2 =[1,11,2,3,4,5]
    result =[1,11,2,3,4,5]
上方的打印结果中，你会发现，使用 sort() 排序后，数字11竟然在数字2的前面。这是为啥呢？因为上面讲到了，sort()方法是按照Unicode编码进行排序的。

那如果我想让 arr2 里的数字，完全按照从小到大排序，怎么操作呢？继续往下看。

sort()方法举例：带参时
如果在 sort()方法中带参，我们就可以自定义排序规则。具体做法如下：

我们可以在sort()添加一个回调函数，来指定排序规则。回调函数中需要定义两个形参，浏览器将会分别使用数组中的元素作为实参去调用回调函数

浏览器根据回调函数的返回值来决定元素的排序：（重要）

如果返回一个大于0的值，则元素会交换位置

如果返回一个小于0的值，则元素位置不变

如果返回一个0，则认为两个元素相等，则不交换位置

代码举例：

    var arr3 = [5, 2, 11, 3, 4, 1];

    // 自定义排序规则
    var result = arr3.sort(function(a, b) {
    if (a > b) { // 如果 a 大于 b，则交换 a 和 b 的位置
      return 1;
    } else if (a < b) { // 如果 a 小于 b，则位置不变
      return -1;
    } else { // 如果 a 等于 b，则位置不变
      return 0;
    }
    });

    console.log("arr3 =" + JSON.stringify(arr3));
    console.log("result =" + JSON.stringify(result));
打印结果：

    arr3 =[1,2,3,4,5,11]
    result =[1,2,3,4,5,11]
上方代码的写法太啰嗦了，其实也可以简化为如下写法：

代码优化：（冒泡排序）

    var arr3 = [5, 2, 11, 3, 4, 1];

    // 自定义排序规则
    var result = arr3.sort(function(a, b) {
    return a - b; // 升序排列
    // return b - a; // 降序排列
    });

    console.log("arr3 =" + JSON.stringify(arr3));
    console.log("result =" + JSON.stringify(result));
打印结果：

    arr3 =[1,2,3,4,5,11]
    result =[1,2,3,4,5,11]