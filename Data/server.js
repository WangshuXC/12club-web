const express = require('express');
const path = require('path');
const app = express();

const cors = require('cors');
app.use(cors());
const AnimesPath = path.join(__dirname, 'Anime');
const MusicPath = path.join(__dirname, 'Music');

app.use('/anime', express.static(AnimesPath));
app.use('/music', express.static(MusicPath));

// 监听端口
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
