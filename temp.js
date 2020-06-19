//0522

const urls = [
  "https://jsonplaceholder.typicode.com/posts",
  "https://jsonplaceholder.typicode.com/comments",
  "https://jsonplaceholder.typicode.com/users",
];

Promise.all(
  urls.map((url) => {
    return fetch(url).then((resp) => resp.json());
  })
)
  .then((array) => {
    console.log("posts", array[0]);
    console.log("comments", array[1]);
    console.log("users", array[2]);
  })
  .catch(console.log("error"));

const getData = async function (urlArray) {
  const [posts, comments, users] = await Promise.all(
    urlArray.map((url) => {
      return fetch(url).then((resp) => resp.json());
    })
  );
  console.log(posts);
  console.log(comments);
  console.log(users);
};

getData(urls);
