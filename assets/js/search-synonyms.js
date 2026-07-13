/* search-synonyms.js — curated bridge between how people ask and how the
 * text says it. Single source of truth: imported by the runtime verse
 * search (search.js, OR-expansion at half weight) AND by the build-time
 * answers-page generator (src/lib/answers-topics.mjs) that fills topics
 * Nave's left as verse-less stubs.
 */
'use strict';

export var SYNONYMS = {
  anxiety:     ['anxious', 'worry', 'worried', 'cares'],
  worry:       ['anxious', 'anxiety', 'cares'],
  anxious:     ['anxiety', 'worry', 'cares'],
  money:       ['riches', 'wealth', 'mammon'],
  wealth:      ['riches', 'money', 'mammon'],
  anger:       ['wrath', 'angry'],
  fear:        ['afraid', 'dread', 'terror'],
  afraid:      ['fear', 'dread'],
  forgiveness: ['forgive', 'forgiven', 'pardon'],
  marriage:    ['marry', 'wife', 'husband'],
  salvation:   ['saved', 'save', 'deliverance'],
  prayer:      ['pray', 'praying', 'supplication'],
  joy:         ['rejoice', 'gladness', 'glad'],
  sin:         ['iniquity', 'transgression', 'trespass'],
  death:       ['die', 'died', 'grave'],
  heaven:      ['heavens', 'paradise'],
  work:        ['labor', 'toil', 'deeds'],
  friendship:  ['friend', 'friends', 'companion'],
  depression:  ['downcast', 'despair', 'sorrow', 'grief'],
  loneliness:  ['alone', 'lonely', 'forsaken'],
  stress:      ['burden', 'weary', 'rest'],
  patience:    ['patient', 'endurance', 'perseverance'],
  temptation:  ['tempted', 'tempt', 'trial'],
  healing:     ['heal', 'healed', 'restore'],
};
