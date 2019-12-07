
window.localStorage.length //3

// 存储某个键值，下面三种写法等价
window.localStorage.foo = '123';
window.localStorage['foo'] = '123';
window.localStorage.setItem('foo', '123');

//移除某一项
sessionStorage.removeItem('key');
localStorage.removeItem('key');

//方法用于清除所有保存的数据。该方法的返回值是undefined。
Storage.clear()
window.sessionStorage.clear()
window.localStorage.clear()

//方法用于读取数据。它只有一个参数，就是键名。如果键名不存在，该方法返回null。
window.sessionStorage.getItem('key')
window.localStorage.getItem('key')
//接受一个整数作为参数（从零开始），返回该位置对应的键值。
Storage.key(0)
//结合使用Storage.length属性和Storage.key()方法，可以遍历所有的键。
for (var i = 0; i < window.localStorage.length; i++) {
  console.log(localStorage.key(i));
}

