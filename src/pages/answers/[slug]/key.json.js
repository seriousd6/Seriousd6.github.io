// /answers/<slug>/key.json — tiny per-topic manifest for search integration.
//
// The verse search renders a topic's key verses INLINE at the top of the
// results (P8) instead of only linking to the answers page. It needs the
// ranked ref list, not the text — the client resolves text from the BSB
// books it already caches. buildAnswerTopics() is memoized, so this endpoint
// adds no extra BSB scan to the build.
import { buildAnswerTopics } from '../../../lib/answers-topics.mjs';

export async function getStaticPaths() {
  return buildAnswerTopics().map((e) => ({
    params: { slug: e.slug },
    props: { title: e.title, refs: e.verses.slice(0, 10), n: e.verses.length },
  }));
}

export async function GET({ props }) {
  return new Response(
    JSON.stringify({ t: props.title, n: props.n, refs: props.refs }),
    { headers: { 'Content-Type': 'application/json' } }
  );
}
