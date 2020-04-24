数组是最常见的数据结构，在不同的语言中，数组有着不同的方法。下面详细阐述js数组的方法：

### 创建一个数组
1. 最简单的方式，也是最常用的：

```javascript
var a = [1,2,3];
```
2. 利用关键词`new`

```javascript
var a = new Array(1,2,3); // a=[1,2,3]
```
3. 实际上`new Array === Array`，加不加`new`，没有任何影响

```javascript
var a = Array(1,2,3); // a=[1,2,3]
```

### 访问一个完整的数组

通过js，可以通过引用数组名访问完整数组：

先获取节点，然后向节点插入数组
```html
<!DOCTYPE html>
<html>
<body>

<p id="demo"></p>

<script>
var cars = ["Audi", "BMW", "porsche"];
document.getElementById("demo").innerHTML = cars;
</script>

</body>
</html>
```

### 数组的属性

