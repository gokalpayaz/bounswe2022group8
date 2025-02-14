import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { HOST } from "../../constants/host";
import Layout from "../../layout/Layout";
import * as dotenv from "dotenv";
import { useAuth } from "../../auth/authentication";

import "../styles/Recommendation.css";

function RecommendedArtitems(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  const navigate = useNavigate();
  const { token } = useAuth();
  var host = HOST;

  const [artItemInfos, setArtItemInfos] = useState([]);
  const [artItemPaths, setArtItemPaths] = useState([]);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  useEffect(() => {
    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/recommendations/artitems/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
         Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        console.log(response.artitems);
        setArtItemInfos(response.artitems);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var art_item_paths = [];

        for (let i = 0; i < response.artitems.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.artitems[i].artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);

          art_item_paths.push(artitem_url);
        }

        setArtItemPaths(art_item_paths);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
    scrollToTop();
  }

  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommendation-grid">
          <h1 className="page-header">Discover Art Items</h1>
          <div className="art-gallery">
            {artItemInfos.map((val, index) => {
              return (
                <div
                  key={val.id}
                  className="recommendation-card"
                  onClick={() => goToArtItem(val.id)}
                >
                  <img
                    className="art-related"
                    src={artItemPaths[index]}
                    alt={val.description}
                  />
                  <div class="artitem-context">
                    <h4>{val.title}</h4>
                    <p>{val.description}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default RecommendedArtitems;
