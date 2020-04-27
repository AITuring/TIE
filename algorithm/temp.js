// var arr = [1, [2, 3, [4, 5, [6]]], 7];


// function getNewArr(arr) {
//     var newArr = [];
//     for (var i = 0; i < arr.length; i++) {
//         if (typeof arr[i] == "number") {
//             newArr.push(arr[i])
//         } else {

//             getNewArr(arr[i])
//         }
//     }
//     return newArr;
// }
// console.log(getNewArr(arr))

// console.log(newArr)

a=[1, -2, 3, 10, -4, 7, 2, -5]
function maxsum(arr) {
    if (arr.length<0){
        return false;
    }
    if (arr.length==0){
        return 0;
    }
    if (arr.length==1){
        return arr[0];
    }
    var cur=arr[0];
    var ans=arr[0];
    for(var i=1;i<arr.length;i++) {
        if(cur <= 0) {
            cur = arr[i];
        } else {
            cur+= arr[i];
        }
        if(cur>ans) {
            ans = cur;
        }
    }
    return ans;
}

console.log(maxsum(a));