/* entries/wordcloud.js — Word-cloud entry (wordcloud/). */
import { boot } from '../core-boot.js';
import { initWordCloudPage } from '../wordcloud.js';

boot(function () {
  initWordCloudPage();
});
