const promise = New Promise((resolve, reject) => {
  if (true){
    resolve('worked');
  }
  else{
    reject('error');
  }
})

promise.then(res => console.log(res))

async function fetchUsers(){
  const resp = await fetch('https://jsonplaceholder.typicode.com/posts');
  const data = await resp.json();
  return data;
}

// test 
// 123123123


obj = {afdfd};
obj2 = { a: 123, b: 456 };
