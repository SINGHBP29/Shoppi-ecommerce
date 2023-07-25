

$('.plus-cart').click(function(){
    // console.log("button click")
    var id=$(this).attr("pid").toString();
    var eml= this.parentNode.children[2]
    console.log("pid =",id)
    $.ajax {{
        type:"GET",
        url;"/pluscart",
        data;{
            prod_id:id
        }
        success:function(data){
            console.log("data = ",data);
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    }}
})

$('.minus-cart').click(function(){
    // console.log("button click")
    var id=$(this).attr("pid").toString();
    var eml= this.parentNode.children[2]
    console.log("pid =",id)
    $.ajax{{
        type:"GET",
        url;"/pluscart",
        data;{
            prod_id:id
        }
        success:function(data){
            console.log("data = ",data);
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    }}
})

$('.remove-cart').click(function(){
    // console.log("button click")
    var id=$(this).attr("pid").toString();
    var eml= this
    console.log("pid =",id)
    $.ajax{{
        type:"GET",
        url;"/pluscart",
        data;{
            prod_id:id
        }
        success:function(data){
            console.log("data = ",data);
            // eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    }}
})

$('.minus-wishlist').click(function(){
     var id=$(this).attr("pid").toString();
     $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = http://localhost:8080/index/$(id)
        }
     })
})

$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
       type:"GET",
       url:"/pluswishlist",
       data:{
           prod_id:id
       },
       success:function(data){
           window.location.href = http://localhost:8080/index/$(id)
       }
    })
})