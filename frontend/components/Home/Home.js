import {PROD_API_KEY, PROD_URL} from '../../config';
import React, { useEffect, useState } from "react";

import {GhostAdminApi} from '@tryghost/admin-api';
import Post from "../Post/Post";

const Home = () => {
  let [posts, setPosts] = useState([]);

   const getPosts = () => {
      api.posts.browse()
        .then(res => res.json())
        .then(posts => setPosts(posts))
        .catch(console.error)

  }

  useEffect(getPosts, []);

  return (
    <div className="home">
      <h1>All Posts</h1>;
      <div className="posts">
        <Post></Post>
        <Post></Post>
        <Post></Post>
      </div>
    </div>
  );
};

export default Home;
