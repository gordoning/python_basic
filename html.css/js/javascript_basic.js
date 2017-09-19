// javascript的基础知识

 // 如何弹出一个对话框
 //    alert("我就是看看javascript555");

// 如何使用正则表达式
    var name = "lgy13616187656";
    var re = /[0-9]{6,20}/;
    if(re.test(name)){
        // alert(name.length);
    }

// 与，或，相等，如何表达，跟python中的语法有何不同吗
    if(true && false){
        console.log('not ok!')
    }
    else if(false || false){
        console.log('success')
    }
    else if(1 === 1){
        console.log('判断成功')
    }

// 如何用模版字符串，来自定义带有变量的字符串
    var name = '林国洋';
    var skill = 'python 和 javascript';
    // var result = '';
    var result = '你好,${name} 正在学习，${skill}';
    result = '你好,'+name+'正在学习'+skill;
    console.log(result);

// 在一个数组中，如何查找某个值是否存在
    var list1 = ['linguoyang',20,'yangfeng',20];
    console.log(list1.indexOf('yangfeng'));

// 修改一个列表的万能方法是什么？（增删改）
    list1.splice(2,1,'abc哈哈');
    console.log(list1);


// 设计一个实例对象,最后一个字符，不可以是什么？
    var linguoyang = {
      name:'linguoyang',
      age:31,
        amazing:'make love'
    };
    console.log(linguoyang['amazing']);

// 循环1-10的语句，该怎么表达:
    for(var i in [1,2,3,4,5,6,7,8,9,10]){
      if(i%3===0){console.log(i);};
    };

    var i = 0;
    for(;;){
      if(i>20){
          break;
      };
      i++;
      if(i%4===0){console.log(i);};
    };


    function add(x,y) {
        // if(x!=='number'){throw 'Not a number99'};
        return x+y;
    }

    console.log(add(parseInt(1),parseInt(5)));