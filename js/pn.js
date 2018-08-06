var button = document.getElementById("button");

button.addEventListener("click", function(b){
    b.preventDefault();

    //textForm
    try{
        var num = document.getElementById("_text").num.value;
        if(isNaN(num)){
            throw new Error("入力した値が数値ではありません");
        }
    }catch(e){
        alert("エラー：" + e.message);
        document.getElementById("_text").num.value = "";
        exit();
    }

    var A = new Array(num + 1)
    for(var i = 0; i <= num; i++){
        A[i] = 1;
    }
    A[0] = 0;
    A[1] = 0;
    for(var i = 2; i <= num; i++){
        if(A[i]){
            for(var j = i * 2; j <= num; j += i){
                A[j] = 0;
            }
        }
    }

    var msg;
    if(A[num]){
        msg = `${num}は素数です`;
    }else{
        msg = `${num}は素数ではない`;
        document.write(msg);
        exit();
    }
    //document.write(msg);

    var cnt = 0;
    for(var i = 2; i <= num; i++){
        if(A[i]) cnt++;
    }

    document.write(`${num}は${cnt}番目の素数です` + "<br>");
    var z = 1;
    for(var i = 2; i <= num; i++){
        if(A[i]){
            document.write(`${z}番目：${i}` + "<br>");
            z++;
        }
    }

});