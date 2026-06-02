"""
MKT John chapters 1-5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-john-1-5.py
"""
import json, os, pathlib

ROOT = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

# ── Translation data ───────────────────────────────────────────────────────
# Three tiers per verse:
#   L = Literal   (word-for-word, Greek structure honored, concepts preserved)
#   M = Mediating (natural but faithful; like ESV/BSB range)
#   T = Thought   (dynamic equivalence; meaning conveyed in natural English)

JOHN = {
  "1": {
    "1": {
      "L": "In the beginning was the Word, and the Word was toward God, and God was the Word.",
      "M": "In the beginning was the Word, and the Word was with God, and the Word was God.",
      "T": "Before time itself began, the divine Word already existed—eternally present with God and fully God in his own nature."
    },
    "2": {
      "L": "This one was in the beginning toward God.",
      "M": "He was with God in the beginning.",
      "T": "This Word was with God from the very beginning."
    },
    "3": {
      "L": "All things came into being through him, and apart from him came into being not one thing that has come into being.",
      "M": "Through him all things were made; without him nothing was made that has been made.",
      "T": "Everything that exists came into being through him—nothing came into existence apart from him."
    },
    "4": {
      "L": "In him was life, and the life was the light of men.",
      "M": "In him was life, and that life was the light of men.",
      "T": "He himself was the source of life, and that life brought light to all humanity."
    },
    "5": {
      "L": "And the light shines in the darkness, and the darkness did not overcome it.",
      "M": "The light shines in the darkness, and the darkness has not overcome it.",
      "T": "This light shines into the darkness, and the darkness has never been able to extinguish it."
    },
    "6": {
      "L": "There came a man sent from God; his name was John.",
      "M": "There was a man sent from God whose name was John.",
      "T": "God sent a man named John as his messenger."
    },
    "7": {
      "L": "This one came for testimony, that he might bear witness concerning the light, so that all might believe through him.",
      "M": "He came as a witness to testify about the Light, so that through him all might believe.",
      "T": "He came to point people to the Light so that through his testimony everyone would come to believe."
    },
    "8": {
      "L": "That one was not the light, but came that he might testify concerning the light.",
      "M": "He himself was not the Light; he came only to testify about the Light.",
      "T": "John was not the Light himself—he was simply a witness sent to testify to the Light."
    },
    "9": {
      "L": "The true light, which enlightens every man, was coming into the world.",
      "M": "The true Light, who gives light to every man, was coming into the world.",
      "T": "The genuine Light—the one who illuminates every person—was entering the world."
    },
    "10": {
      "L": "He was in the world, and the world came into being through him, yet the world did not know him.",
      "M": "He was in the world, and though the world was made through him, the world did not recognize him.",
      "T": "He was present in the world—the very world he had made—yet the world failed to recognize him."
    },
    "11": {
      "L": "He came to his own domain, and his own people did not receive him.",
      "M": "He came to his own, and his own people did not receive him.",
      "T": "He came to the very people who belonged to him, but they refused to accept him."
    },
    "12": {
      "L": "But as many as received him, to them he gave authority to become children of God—to those who believe into his name.",
      "M": "Yet to all who received him, to those who believed in his name, he gave the right to become children of God.",
      "T": "But to everyone who did receive him—everyone who trusted in who he is—he gave the right to become God's own children."
    },
    "13": {
      "L": "Who were born not from bloodlines, nor from the will of the flesh, nor from the will of man, but from God.",
      "M": "These were born not of blood, nor of human decision or a husband's will, but born of God.",
      "T": "This birth doesn't come through human ancestry, physical impulse, or any human decision—it comes entirely from God."
    },
    "14": {
      "L": "And the Word became flesh and tabernacled among us, and we beheld his glory—glory as of the only-begotten from the Father—full of grace and truth.",
      "M": "The Word became flesh and made his dwelling among us, and we have seen his glory—the glory of the one and only Son from the Father—full of grace and truth.",
      "T": "The Word became a human being and pitched his tent among us. We saw his glory with our own eyes—the glory that belongs to the Father's unique Son—overflowing with grace and truth."
    },
    "15": {
      "L": "John testifies concerning him and has cried out, saying: 'This was the one of whom I said, He who comes after me has been before me, because he was first of me.'",
      "M": "John testified about him and cried out, 'This is he of whom I said, He who comes after me has surpassed me, because he existed before me.'",
      "T": "John declared publicly about him: 'This is the one I meant when I said, He who comes after me has surpassed me, because he existed long before I was born.'"
    },
    "16": {
      "L": "Because from his fullness we all have received, even grace upon grace.",
      "M": "For from his fullness we have all received, grace upon grace.",
      "T": "Out of his inexhaustible fullness we have all received wave upon wave of grace."
    },
    "17": {
      "L": "Because the Law was given through Moses; grace and truth came through Jesus Christ.",
      "M": "For the Law was given through Moses; grace and truth came through Jesus Christ.",
      "T": "God gave us the Law through Moses, but grace and truth arrived through Jesus Christ."
    },
    "18": {
      "L": "God no one has ever seen; the only-begotten God, who is in the bosom of the Father—that one has made him known.",
      "M": "No one has ever seen God; the only-begotten God, who is at the Father's side, has made him known.",
      "T": "No human being has ever seen God. But the unique Son—who is himself God and lives in the closest intimacy with the Father—he has fully revealed him to us."
    },
    "19": {
      "L": "And this is the testimony of John, when the Jews sent from Jerusalem priests and Levites to ask him, 'Who are you?'",
      "M": "Now this was John's testimony when the Jewish leaders in Jerusalem sent priests and Levites to ask him who he was.",
      "T": "Here is the testimony John gave when the Jewish authorities sent a delegation of priests and Levites from Jerusalem to ask him, 'Who are you?'"
    },
    "20": {
      "L": "And he confessed—and did not deny—and confessed: 'I am not the Christ.'",
      "M": "He confessed freely and did not deny it, but confessed plainly, 'I am not the Messiah.'",
      "T": "He answered without hedging or evasion: 'I am not the Messiah.'"
    },
    "21": {
      "L": "And they asked him: 'What then? Are you Elijah?' And he says, 'I am not.' 'Are you the Prophet?' And he answered, 'No.'",
      "M": "So they asked him, 'Then who are you? Are you Elijah?' 'I am not,' he said. 'Are you the Prophet?' 'No,' he answered.",
      "T": "'Then who are you?' they pressed. 'Are you Elijah?' 'No.' 'Are you the Prophet?' 'No.'"
    },
    "22": {
      "L": "Then they said to him: 'Who are you? So that we may give an answer to those who sent us. What do you say about yourself?'",
      "M": "Finally they said, 'Who are you? We need to give an answer to those who sent us. What do you say about yourself?'",
      "T": "They pushed further: 'Then tell us who you are—we have to report back to those who sent us. How would you describe yourself?'"
    },
    "23": {
      "L": "He said: 'I am a voice of one crying in the wilderness: Make straight the way of the Lord—as Isaiah the prophet said.'",
      "M": "He replied in the words of Isaiah the prophet: 'I am the voice of one calling in the wilderness, Make straight the way of the Lord.'",
      "T": "He answered with the words of Isaiah: 'I am a voice shouting in the wilderness: Clear the road for the Lord!'"
    },
    "24": {
      "L": "Now those who had been sent were from the Pharisees.",
      "M": "Now some Pharisees were among those sent.",
      "T": "The delegation included representatives from the Pharisees."
    },
    "25": {
      "L": "And they asked him and said to him: 'Why then do you baptize, if you are not the Christ, nor Elijah, nor the Prophet?'",
      "M": "They questioned him further: 'Then why do you baptize, if you are not the Messiah, nor Elijah, nor the Prophet?'",
      "T": "'If you're none of those,' they challenged, 'then why are you baptizing people?'"
    },
    "26": {
      "L": "John answered them saying: 'I baptize with water; but in your midst stands one whom you do not know—'",
      "M": "John answered them, 'I baptize with water, but among you stands one you do not know.'",
      "T": "John told them: 'My baptism is only water. But there is someone standing right among you whom you don't yet recognize—'"
    },
    "27": {
      "L": "'—the one coming after me, of whom I am not worthy to loosen the strap of his sandal.'",
      "M": "'He is the one who comes after me, the straps of whose sandals I am not worthy to untie.'",
      "T": "'He comes after me, but he is so far above me that I am not worthy to untie his sandals.'"
    },
    "28": {
      "L": "These things happened in Bethany beyond the Jordan, where John was baptizing.",
      "M": "All this took place at Bethany on the other side of the Jordan, where John was baptizing.",
      "T": "This exchange took place at Bethany on the far side of the Jordan River, where John was conducting his baptisms."
    },
    "29": {
      "L": "On the next day he sees Jesus coming toward him and says: 'Look! The Lamb of God who takes away the sin of the world!'",
      "M": "The next day John saw Jesus coming toward him and said, 'Look, the Lamb of God, who takes away the sin of the world!'",
      "T": "The following day John saw Jesus approaching and announced: 'Look—God's Lamb! The one who removes the world's sin!'"
    },
    "30": {
      "L": "This is he of whom I said: 'After me comes a man who has been before me, because he was first of me.'",
      "M": "This is the one I meant when I said, 'A man who comes after me has surpassed me because he existed before me.'",
      "T": "He is the one I was speaking about: 'Someone comes after me who is far greater than I am, because he existed long before I did.'"
    },
    "31": {
      "L": "And I myself did not know him, but so that he might be made manifest to Israel—for this reason I came baptizing with water.",
      "M": "I myself did not know him, but the reason I came baptizing with water was that he might be revealed to Israel.",
      "T": "I had no idea who he was—but my water baptism was God's plan to make him known to Israel."
    },
    "32": {
      "L": "And John testified, saying: 'I have seen the Spirit descending like a dove from heaven, and it remained upon him.'",
      "M": "Then John testified: 'I saw the Spirit descend from heaven like a dove, and he remained on him.'",
      "T": "John declared: 'I saw the Spirit descend from heaven like a dove and settle upon him and stay.'"
    },
    "33": {
      "L": "And I myself did not know him, but the one who sent me to baptize with water—that one said to me: 'Upon whom you see the Spirit descending and remaining on him, this is the one who baptizes with the Holy Spirit.'",
      "M": "I would not have known him, except that the one who sent me to baptize with water told me: 'The man on whom you see the Spirit descend and remain is he who baptizes with the Holy Spirit.'",
      "T": "I wouldn't have recognized him on my own—but the one who sent me to baptize had told me: 'The man on whom you see the Spirit descend and rest, he is the one who baptizes in the Holy Spirit.'"
    },
    "34": {
      "L": "And I myself have seen and have testified that this is the Son of God.",
      "M": "I have seen and I testify that this is the Son of God.",
      "T": "I witnessed it myself, and I am now declaring: this is the Son of God."
    },
    "35": {
      "L": "Again on the next day John was standing with two of his disciples.",
      "M": "The following day John was there again with two of his disciples.",
      "T": "The next day John was standing there again with two of his disciples."
    },
    "36": {
      "L": "And having looked intently at Jesus walking he says: 'Look! The Lamb of God!'",
      "M": "When he saw Jesus passing by, he said, 'Look, the Lamb of God!'",
      "T": "He watched Jesus walk past and said, 'Look—God's Lamb!'"
    },
    "37": {
      "L": "And the two disciples heard him speaking, and they followed Jesus.",
      "M": "When the two disciples heard him say this, they followed Jesus.",
      "T": "The two disciples heard this and immediately began to follow Jesus."
    },
    "38": {
      "L": "Then Jesus turned and, having seen them following, says to them: 'What are you seeking?' And they said to him: 'Rabbi'—which translated means Teacher—'where are you staying?'",
      "M": "Jesus turned and saw them following and asked, 'What do you want?' They said, 'Rabbi' (which means Teacher), 'where are you staying?'",
      "T": "Jesus turned, saw them following, and asked, 'What are you looking for?' 'Rabbi,' they answered (which means Teacher), 'where are you staying?'"
    },
    "39": {
      "L": "He says to them: 'Come and you will see.' So they came and saw where he was staying, and they remained with him that day. The hour was about the tenth.",
      "M": "He said to them, 'Come and you will see.' So they went and saw where he was staying, and they spent that day with him. It was about the tenth hour.",
      "T": "'Come and see,' he replied. They went, saw where he was living, and stayed with him the rest of the day. It was about four in the afternoon."
    },
    "40": {
      "L": "Andrew, the brother of Simon Peter, was one of the two who heard from John and followed him.",
      "M": "Andrew, Simon Peter's brother, was one of the two who heard what John said and followed Jesus.",
      "T": "Andrew, Simon Peter's brother, was one of these two who had heard John's testimony and then followed Jesus."
    },
    "41": {
      "L": "This one first finds his own brother Simon and says to him: 'We have found the Messiah!'—which translated is Christ.",
      "M": "He first found his own brother Simon and told him, 'We have found the Messiah!' (which is translated Christ).",
      "T": "The first thing Andrew did was find his brother Simon and tell him, 'We've found the Messiah!' (That is, the Christ.)"
    },
    "42": {
      "L": "He led him to Jesus. Having looked at him, Jesus said: 'You are Simon the son of John; you shall be called Cephas'—which is translated Peter.",
      "M": "And he brought him to Jesus. Jesus looked at him and said, 'You are Simon son of John. You will be called Cephas' (which, when translated, is Peter).",
      "T": "Andrew brought him to Jesus. Jesus looked straight at him and said, 'You are Simon, son of John. Your new name will be Cephas'—that is, Peter, which means Rock."
    },
    "43": {
      "L": "On the next day Jesus wished to go into Galilee, and he finds Philip. And Jesus says to him: 'Follow me.'",
      "M": "The next day Jesus decided to leave for Galilee and found Philip. Jesus said to him, 'Follow me.'",
      "T": "The next day Jesus decided to head into Galilee. He found Philip and said simply, 'Follow me.'"
    },
    "44": {
      "L": "Now Philip was from Bethsaida, the city of Andrew and Peter.",
      "M": "Philip, like Andrew and Peter, was from the town of Bethsaida.",
      "T": "Philip was from Bethsaida, the same hometown as Andrew and Peter."
    },
    "45": {
      "L": "Philip finds Nathanael and says to him: 'The one about whom Moses wrote in the Law, and also the prophets, we have found—Jesus the son of Joseph, who is from Nazareth.'",
      "M": "Philip found Nathanael and told him, 'We have found the one Moses wrote about in the Law, and about whom the prophets also wrote—Jesus of Nazareth, the son of Joseph.'",
      "T": "Philip found Nathanael and announced, 'We've found the one Moses wrote about in the Law and the prophets described—Jesus of Nazareth, son of Joseph!'"
    },
    "46": {
      "L": "And Nathanael said to him: 'Can any good thing come out of Nazareth?' Philip says to him: 'Come and see.'",
      "M": "Nathanael replied, 'Can anything good come from Nazareth?' 'Come and see,' Philip answered.",
      "T": "Nathanael scoffed, 'Nazareth? Can anything good come from there?' Philip simply replied, 'Come and find out.'"
    },
    "47": {
      "L": "Jesus saw Nathanael coming toward him and says about him: 'Behold, truly an Israelite in whom there is no deceit.'",
      "M": "When Jesus saw Nathanael approaching, he said of him, 'Here is a true Israelite, in whom there is nothing false.'",
      "T": "When Jesus saw Nathanael coming toward him, he said, 'Here is a genuine son of Israel—a man with no hidden agenda.'"
    },
    "48": {
      "L": "Nathanael says to him: 'From where do you know me?' Jesus answered and said to him: 'Before Philip called you, when you were under the fig tree, I saw you.'",
      "M": "Nathanael asked him, 'How do you know me?' Jesus answered, 'I saw you while you were still under the fig tree before Philip called you.'",
      "T": "'How do you know anything about me?' Nathanael asked. Jesus replied, 'I saw you sitting under the fig tree before Philip ever called you.'"
    },
    "49": {
      "L": "Nathanael answered him: 'Rabbi, you are the Son of God! You are the King of Israel!'",
      "M": "Then Nathanael declared, 'Rabbi, you are the Son of God! You are the King of Israel!'",
      "T": "Nathanael burst out, 'Teacher! You are the Son of God—the King of Israel!'"
    },
    "50": {
      "L": "Jesus answered and said to him: 'Because I said to you that I saw you under the fig tree—you believe? You will see greater things than these.'",
      "M": "Jesus replied, 'You believe because I told you I saw you under the fig tree. You will see greater things than that.'",
      "T": "Jesus replied, 'You believe just because I told you I saw you under the fig tree? You haven't seen anything yet.'"
    },
    "51": {
      "L": "And he says to him: 'Truly, truly I say to you—you will see heaven opened and the angels of God ascending and descending upon the Son of Man.'",
      "M": "He then added, 'Truly, truly, I tell you, you will see heaven opened, and the angels of God ascending and descending on the Son of Man.'",
      "T": "Then he told him, 'I am absolutely certain: you will see heaven standing open, with God's angels ascending and descending upon the Son of Man.'"
    }
  },

  "2": {
    "1": {
      "L": "And on the third day there was a wedding in Cana of Galilee, and the mother of Jesus was there.",
      "M": "On the third day a wedding took place at Cana in Galilee, and the mother of Jesus was there.",
      "T": "Three days later there was a wedding celebration in Cana of Galilee, and Jesus' mother was among the guests."
    },
    "2": {
      "L": "And Jesus too was invited, together with his disciples, to the wedding.",
      "M": "Jesus and his disciples had also been invited to the wedding.",
      "T": "Jesus and his disciples had been invited as well."
    },
    "3": {
      "L": "And when the wine ran out, the mother of Jesus says to him: 'They have no wine.'",
      "M": "When the wine ran out, Jesus' mother said to him, 'They have no more wine.'",
      "T": "When the wine ran out, Jesus' mother came to him and said, 'They've run out of wine.'"
    },
    "4": {
      "L": "And Jesus says to her: 'What is that to me and to you, woman? My hour has not yet come.'",
      "M": "Jesus replied, 'Woman, why do you involve me? My hour has not yet come.'",
      "T": "Jesus said to her, 'Dear woman, that is not our concern. My time has not yet come.'"
    },
    "5": {
      "L": "His mother says to the servants: 'Whatever he tells you, do it.'",
      "M": "His mother said to the servants, 'Do whatever he tells you.'",
      "T": "But his mother told the servants, 'Do whatever he says.'"
    },
    "6": {
      "L": "Now there were six stone water jars set there for the Jewish purification rites, each holding two or three measures.",
      "M": "Nearby stood six stone water jars, the kind used by the Jews for ceremonial washing, each holding twenty to thirty gallons.",
      "T": "Standing nearby were six large stone water jars used for Jewish purification rituals, each holding twenty to thirty gallons."
    },
    "7": {
      "L": "Jesus says to them: 'Fill the water jars with water.' And they filled them to the brim.",
      "M": "Jesus said to the servants, 'Fill the jars with water.' So they filled them to the brim.",
      "T": "Jesus told the servants, 'Fill the jars with water,' and they filled every one of them to the very top."
    },
    "8": {
      "L": "And he says to them: 'Now draw some out and carry it to the master of the feast.' And they carried it.",
      "M": "Then he told them, 'Now draw some out and take it to the master of the banquet.' They did so.",
      "T": "Then he said, 'Now scoop some out and take it to the banquet master.' And they did."
    },
    "9": {
      "L": "When the master of the feast tasted the water that had become wine—and did not know where it came from, though the servants who had drawn the water knew—the master of the feast calls the bridegroom",
      "M": "When the master of the banquet tasted the water that had been turned into wine, he did not know where it came from, though the servants who had drawn the water knew. Then he called the bridegroom aside",
      "T": "The banquet master tasted the water that had become wine. He had no idea where it came from—though the servants knew—so he called the bridegroom over"
    },
    "10": {
      "L": "and says to him: 'Every man serves the good wine first, and when they have drunk freely, the inferior. You have kept the good wine until now.'",
      "M": "and said, 'Everyone brings out the choice wine first and then the cheaper wine after the guests have had too much to drink; but you have saved the best till now.'",
      "T": "and said to him, 'Everyone serves the best wine first, and after guests have had plenty, brings out the cheaper wine. But you have saved the finest wine for now!'"
    },
    "11": {
      "L": "This beginning of signs Jesus did in Cana of Galilee, and he revealed his glory; and his disciples believed in him.",
      "M": "What Jesus did here in Cana of Galilee was the first of the signs through which he revealed his glory; and his disciples believed in him.",
      "T": "This was the first miraculous sign Jesus performed—here in Cana of Galilee—and through it he revealed his glory, and his disciples put their faith in him."
    },
    "12": {
      "L": "After this he went down to Capernaum, he and his mother and his brothers and his disciples, and they stayed there not many days.",
      "M": "After this he went down to Capernaum with his mother, his brothers, and his disciples, and they stayed there for a few days.",
      "T": "After the wedding, Jesus went to Capernaum with his mother, his brothers, and his disciples, and they stayed for a few days."
    },
    "13": {
      "L": "And the Passover of the Jews was near, and Jesus went up to Jerusalem.",
      "M": "When it was almost time for the Jewish Passover, Jesus went up to Jerusalem.",
      "T": "The Jewish Passover was approaching, so Jesus traveled up to Jerusalem."
    },
    "14": {
      "L": "And in the temple he found those selling oxen and sheep and doves, and the money-changers sitting there.",
      "M": "In the temple courts he found people selling cattle, sheep and doves, and others sitting at tables exchanging money.",
      "T": "In the temple courts he found merchants selling cattle, sheep, and doves, with money-changers sitting at their tables."
    },
    "15": {
      "L": "And having made a whip of cords, he drove them all out of the temple—both the sheep and the oxen—and he poured out the coins of the money-changers and overturned the tables.",
      "M": "So he made a whip out of cords and drove all from the temple courts, both sheep and cattle; he scattered the coins of the money changers and overturned their tables.",
      "T": "He made a whip from some rope and drove them all out of the temple—animals and merchants alike. He sent the coins of the money-changers flying and knocked their tables over."
    },
    "16": {
      "L": "And to those selling doves he said: 'Take these things out of here! Stop making my Father's house a marketplace!'",
      "M": "To those who sold doves he said, 'Get these out of here! Stop turning my Father's house into a market!'",
      "T": "He told the dove sellers, 'Get all this out of here! Don't turn my Father's house into a marketplace!'"
    },
    "17": {
      "L": "His disciples remembered that it was written: 'Zeal for your house will consume me.'",
      "M": "His disciples remembered that it is written: 'Zeal for your house will consume me.'",
      "T": "This brought to his disciples' minds the scripture: 'Passionate devotion for your house will consume me.'"
    },
    "18": {
      "L": "Therefore the Jews answered and said to him: 'What sign do you show us, since you do these things?'",
      "M": "The Jews then responded to him, 'What sign can you show us to prove your authority to do all this?'",
      "T": "The Jewish leaders demanded, 'What miraculous sign can you show us to prove you have authority to do this?'"
    },
    "19": {
      "L": "Jesus answered and said to them: 'Destroy this temple, and in three days I will raise it up.'",
      "M": "Jesus answered them, 'Destroy this temple, and I will raise it again in three days.'",
      "T": "Jesus replied, 'Tear down this temple and in three days I will rebuild it.'"
    },
    "20": {
      "L": "Therefore the Jews said: 'Forty-six years this temple was built, and you will raise it up in three days?'",
      "M": "They replied, 'It has taken forty-six years to build this temple, and you are going to raise it in three days?'",
      "T": "They scoffed, 'It took forty-six years to build this temple, and you're going to rebuild it in three days?'"
    },
    "21": {
      "L": "But that one was speaking about the temple of his body.",
      "M": "But the temple he had spoken of was his body.",
      "T": "But the temple he was speaking about was his own body."
    },
    "22": {
      "L": "Therefore when he was raised from the dead, his disciples remembered that he had said this; and they believed the scripture and the word that Jesus had spoken.",
      "M": "After he was raised from the dead, his disciples recalled what he had said. Then they believed the scripture and the words that Jesus had spoken.",
      "T": "After his resurrection, his disciples remembered he had said this, and they believed both the scripture and what Jesus had told them."
    },
    "23": {
      "L": "Now while he was in Jerusalem at the Passover, during the feast, many believed in his name, seeing his signs that he was doing.",
      "M": "Now while he was in Jerusalem at the Passover Festival, many people saw the signs he was performing and believed in his name.",
      "T": "During the Passover festival in Jerusalem, many people saw the miraculous signs he was doing and put their faith in him."
    },
    "24": {
      "L": "But Jesus himself did not entrust himself to them, because he knew all men,",
      "M": "But Jesus would not entrust himself to them, for he knew all people.",
      "T": "But Jesus did not entrust himself to them, because he knew what people are really like."
    },
    "25": {
      "L": "and because he had no need that anyone testify concerning man, for he himself knew what was in man.",
      "M": "He did not need any testimony about mankind, for he knew what was in each person.",
      "T": "He had no need for anyone to give him a report on human nature—he already knew what was inside every person."
    }
  },

  "3": {
    "1": {
      "L": "Now there was a man of the Pharisees named Nicodemus, a ruler of the Jews.",
      "M": "Now there was a Pharisee, a man named Nicodemus who was a member of the Jewish ruling council.",
      "T": "There was a man named Nicodemus, a Pharisee and a member of the Jewish ruling council."
    },
    "2": {
      "L": "This one came to him at night and said to him: 'Rabbi, we know that you have come from God as a teacher; for no one can do these signs that you do unless God is with him.'",
      "M": "He came to Jesus at night and said, 'Rabbi, we know that you are a teacher who has come from God. For no one could perform the signs you are doing if God were not with him.'",
      "T": "He came to Jesus at night and said, 'Rabbi, we know you are a teacher who comes from God—no one could perform the signs you're performing if God were not with him.'"
    },
    "3": {
      "L": "Jesus answered and said to him: 'Truly, truly I say to you, unless one is born from above, he is not able to see the kingdom of God.'",
      "M": "Jesus replied, 'Truly, truly, I tell you, no one can see the kingdom of God unless they are born again.'",
      "T": "Jesus answered him, 'I tell you the absolute truth: no one can see God's kingdom without being born from above.'"
    },
    "4": {
      "L": "Nicodemus says to him: 'How can a man be born when he is old? Can he enter a second time into his mother's womb and be born?'",
      "M": "Nicodemus asked, 'How can someone be born when they are old? Surely they cannot enter a second time into their mother's womb to be born!'",
      "T": "Nicodemus asked, 'How can a man be born when he is already old? He can't go back into his mother's womb and be born again, can he?'"
    },
    "5": {
      "L": "Jesus answered: 'Truly, truly I say to you, unless one is born of water and Spirit, he is not able to enter the kingdom of God.'",
      "M": "Jesus answered, 'Truly, truly, I tell you, no one can enter the kingdom of God unless they are born of water and the Spirit.'",
      "T": "Jesus answered, 'I am telling you the truth: no one can enter God's kingdom without being born of water and the Spirit.'"
    },
    "6": {
      "L": "'That which is born of the flesh is flesh, and that which is born of the Spirit is spirit.'",
      "M": "'Flesh gives birth to flesh, but the Spirit gives birth to spirit.'",
      "T": "'Physical birth produces a physical person; spiritual birth produces a spiritual person.'"
    },
    "7": {
      "L": "'Do not be astonished that I said to you: You must be born from above.'",
      "M": "'You should not be surprised at my saying, You must be born again.'",
      "T": "'Don't be surprised that I told you this: you must all be born from above.'"
    },
    "8": {
      "L": "'The wind blows where it wishes, and you hear its sound, but you do not know where it comes from or where it goes. So it is with everyone born of the Spirit.'",
      "M": "'The wind blows wherever it pleases. You hear its sound, but you cannot tell where it comes from or where it is going. So it is with everyone born of the Spirit.'",
      "T": "'The wind blows wherever it wants. You can hear it, but you can't tell where it comes from or where it's going. That's how it is with everyone born of the Spirit.'"
    },
    "9": {
      "L": "Nicodemus answered and said to him: 'How can these things come to be?'",
      "M": "'How can this be?' Nicodemus asked.",
      "T": "'How is this possible?' Nicodemus asked."
    },
    "10": {
      "L": "Jesus answered and said to him: 'Are you the teacher of Israel and you do not know these things?'",
      "M": "'You are Israel's teacher,' said Jesus, 'and you do not understand these things?'",
      "T": "Jesus replied, 'You are Israel's recognized teacher, and you don't understand this?'"
    },
    "11": {
      "L": "'Truly, truly I say to you, that we speak what we know, and we testify to what we have seen; and our testimony you do not receive.'",
      "M": "'Truly, truly, I tell you, we speak of what we know, and we testify to what we have seen, but still you people do not accept our testimony.'",
      "T": "'I'm telling you the truth: we speak of what we know and testify to what we have seen, but you won't accept what we say.'"
    },
    "12": {
      "L": "'If I told you earthly things and you do not believe, how will you believe if I tell you heavenly things?'",
      "M": "'I have spoken to you of earthly things and you do not believe; how then will you believe if I speak of heavenly things?'",
      "T": "'If you don't believe me when I talk about things happening here on earth, how will you believe me when I speak about heaven?'"
    },
    "13": {
      "L": "'And no one has ascended into heaven except the one who descended from heaven—the Son of Man.'",
      "M": "'No one has ever gone into heaven except the one who came from heaven—the Son of Man.'",
      "T": "'No one has gone up to heaven except the one who came down from heaven—the Son of Man.'"
    },
    "14": {
      "L": "'And just as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up,'",
      "M": "'Just as Moses lifted up the snake in the wilderness, so the Son of Man must be lifted up,'",
      "T": "'Just as Moses lifted up the bronze snake on a pole in the wilderness, the Son of Man must be lifted up in the same way—'"
    },
    "15": {
      "L": "'so that everyone who believes in him may have eternal life.'",
      "M": "'that everyone who believes may have eternal life in him.'",
      "T": "'so that everyone who trusts in him will have eternal life.'"
    },
    "16": {
      "L": "For in this way God loved the world: he gave his only-begotten Son, so that everyone who believes in him should not perish but have eternal life.",
      "M": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
      "T": "For this is how much God loved the world: he gave his one and only Son, so that everyone who trusts in him will not be destroyed but will have eternal life."
    },
    "17": {
      "L": "For God did not send the Son into the world in order to judge the world, but so that the world might be saved through him.",
      "M": "For God did not send his Son into the world to condemn the world, but to save the world through him.",
      "T": "God did not send his Son into the world to condemn the world, but to rescue the world through him."
    },
    "18": {
      "L": "The one who believes in him is not judged; but the one who does not believe has already been judged, because he has not believed in the name of the only-begotten Son of God.",
      "M": "Whoever believes in him is not condemned, but whoever does not believe stands condemned already because they have not believed in the name of God's one and only Son.",
      "T": "Anyone who trusts in him is not condemned. But anyone who refuses to trust is already condemned, because they have not believed in the name of God's unique Son."
    },
    "19": {
      "L": "And this is the judgment: the light has come into the world, and men loved the darkness rather than the light, because their works were evil.",
      "M": "This is the verdict: Light has come into the world, but people loved darkness instead of light because their deeds were evil.",
      "T": "And the judgment is this: the Light came into the world, but people loved the darkness rather than the Light, because what they were doing was wrong."
    },
    "20": {
      "L": "For everyone who practices evil hates the light and does not come to the light, so that his works will not be exposed.",
      "M": "Everyone who does evil hates the light, and will not come into the light for fear that their deeds will be exposed.",
      "T": "People who do wrong hate the light and avoid it, because they don't want their actions exposed."
    },
    "21": {
      "L": "But the one who does the truth comes to the light, so that his works may be made manifest, that they have been wrought in God.",
      "M": "But whoever lives by the truth comes into the light, so that it may be seen plainly that what they have done has been done in the sight of God.",
      "T": "But those who live by the truth gladly come to the light, because the light shows that what they are doing is from God."
    },
    "22": {
      "L": "After these things Jesus and his disciples came into the land of Judea, and there he spent time with them and was baptizing.",
      "M": "After this, Jesus and his disciples went out into the Judean countryside, where he spent some time with them, and baptized.",
      "T": "After this Jesus went with his disciples into the Judean countryside, where he spent time with them, and people were being baptized."
    },
    "23": {
      "L": "Now John also was baptizing at Aenon near Salim, because water was plentiful there, and people were coming and being baptized.",
      "M": "Now John also was baptizing at Aenon near Salim, because there was plenty of water there, and people were coming and being baptized.",
      "T": "John was also baptizing at Aenon near Salim, because there was an abundant water supply there, and crowds kept coming to be baptized."
    },
    "24": {
      "L": "For John had not yet been thrown into prison.",
      "M": "This was before John was put in prison.",
      "T": "This was before John was put in prison."
    },
    "25": {
      "L": "There arose therefore a discussion on the part of John's disciples with a Jew about purification.",
      "M": "An argument developed between some of John's disciples and a certain Jew over the matter of ceremonial washing.",
      "T": "A dispute arose between some of John's disciples and a Jewish man about ritual purification."
    },
    "26": {
      "L": "And they came to John and said to him: 'Rabbi, the one who was with you beyond the Jordan, to whom you have testified—look, he is baptizing, and all are going to him.'",
      "M": "They came to John and said to him, 'Rabbi, that man who was with you on the other side of the Jordan—the one you testified about—look, he is baptizing, and everyone is going to him.'",
      "T": "They came to John with the complaint: 'Rabbi, the man you testified about beyond the Jordan—he is now baptizing, and everyone is going to him!'"
    },
    "27": {
      "L": "John answered and said: 'A man can receive nothing unless it has been given to him from heaven.'",
      "M": "To this John replied, 'A person can receive only what is given them from heaven.'",
      "T": "John answered, 'A person can only receive what is given to them from heaven.'"
    },
    "28": {
      "L": "'You yourselves bear witness that I said: I am not the Christ, but that I have been sent before him.'",
      "M": "'You yourselves can testify that I said, I am not the Messiah but am sent ahead of him.'",
      "T": "'You can back me up on this—I told you clearly: I am not the Messiah. I was sent ahead of him to prepare the way.'"
    },
    "29": {
      "L": "'The one who has the bride is the bridegroom; but the friend of the bridegroom, the one who stands and hears him, rejoices greatly because of the bridegroom's voice. Therefore this joy of mine has been made full.'",
      "M": "'The bride belongs to the bridegroom. The friend who attends the bridegroom waits and listens for him, and is full of joy when he hears the bridegroom's voice. That joy is mine, and it is now complete.'",
      "T": "'The groom is the one who gets the bride. The best man stands nearby and listens, and he is overjoyed when he hears the groom's voice. That is the kind of joy I feel right now, and my joy is complete.'"
    },
    "30": {
      "L": "'He must increase, but I must decrease.'",
      "M": "'He must become greater; I must become less.'",
      "T": "'He must increase in importance; I must fade into the background.'"
    },
    "31": {
      "L": "The one who comes from above is above all; the one who is from the earth is earthly and speaks of earthly things. The one who comes from heaven is above all.",
      "M": "The one who comes from above is above all; the one who is from the earth belongs to the earth, and speaks as one from the earth. The one who comes from heaven is above all.",
      "T": "The one who comes from above is greater than all. The one who is from the earth thinks and speaks in earthly terms. The one who comes from heaven is above all."
    },
    "32": {
      "L": "What he has seen and heard—this he testifies to; and no one accepts his testimony.",
      "M": "He testifies to what he has seen and heard, but no one accepts his testimony.",
      "T": "He speaks of what he has seen and heard, yet hardly anyone accepts what he says."
    },
    "33": {
      "L": "The one who has accepted his testimony has set his seal that God is true.",
      "M": "Whoever has accepted it has certified that God is truthful.",
      "T": "But whoever does accept his testimony has declared that God is trustworthy."
    },
    "34": {
      "L": "For the one whom God sent speaks the words of God, for he gives the Spirit without measure.",
      "M": "For the one whom God has sent speaks the words of God, for God gives the Spirit without limit.",
      "T": "The one God sent speaks God's very words, because God gives his Spirit without limit."
    },
    "35": {
      "L": "The Father loves the Son and has given all things into his hand.",
      "M": "The Father loves the Son and has placed everything in his hands.",
      "T": "The Father loves the Son and has entrusted everything to him."
    },
    "36": {
      "L": "The one who believes in the Son has eternal life; but the one who disobeys the Son will not see life—the wrath of God remains on him.",
      "M": "Whoever believes in the Son has eternal life, but whoever rejects the Son will not see life, for God's wrath remains on them.",
      "T": "Anyone who trusts in the Son already possesses eternal life. Anyone who refuses to trust the Son will never see life—God's judgment stays on them."
    }
  },

  "4": {
    "1": {
      "L": "Therefore, when the Lord knew that the Pharisees had heard that Jesus was making and baptizing more disciples than John",
      "M": "Now Jesus learned that the Pharisees had heard that he was gaining and baptizing more disciples than John—",
      "T": "Jesus knew the Pharisees had heard that he was baptizing and gaining more followers than John."
    },
    "2": {
      "L": "(though Jesus himself was not baptizing but his disciples),",
      "M": "although in fact it was not Jesus who baptized, but his disciples.",
      "T": "(Though it was actually his disciples doing the baptizing, not Jesus himself.)"
    },
    "3": {
      "L": "he left Judea and departed again into Galilee.",
      "M": "So he left Judea and went back once more to Galilee.",
      "T": "He left Judea and headed back to Galilee."
    },
    "4": {
      "L": "And it was necessary for him to pass through Samaria.",
      "M": "Now he had to go through Samaria.",
      "T": "His route took him through Samaria."
    },
    "5": {
      "L": "So he comes to a city of Samaria called Sychar, near the plot of land that Jacob gave to Joseph his son.",
      "M": "So he came to a town in Samaria called Sychar, near the plot of ground Jacob had given to his son Joseph.",
      "T": "He arrived at a Samaritan town called Sychar, near the field that Jacob had given to his son Joseph."
    },
    "6": {
      "L": "Jacob's well was there; and Jesus, wearied from the journey, was sitting thus at the well. The hour was about the sixth.",
      "M": "Jacob's well was there, and Jesus, tired as he was from the journey, sat down by the well. It was about noon.",
      "T": "Jacob's well was there. Jesus, exhausted from the journey, sat down beside the well. It was about noon."
    },
    "7": {
      "L": "There comes a woman of Samaria to draw water. Jesus says to her: 'Give me a drink.'",
      "M": "When a Samaritan woman came to draw water, Jesus said to her, 'Will you give me a drink?'",
      "T": "A Samaritan woman came to draw water, and Jesus said to her, 'Please give me a drink.'"
    },
    "8": {
      "L": "For his disciples had gone into the city to buy food.",
      "M": "(His disciples had gone into town to buy food.)",
      "T": "His disciples had gone into town to buy food."
    },
    "9": {
      "L": "Therefore the Samaritan woman says to him: 'How is it that you, a Jew, ask a drink from me, a Samaritan woman?' For Jews have no dealings with Samaritans.",
      "M": "The Samaritan woman said to him, 'You are a Jew and I am a Samaritan woman. How can you ask me for a drink?' (For Jews do not associate with Samaritans.)",
      "T": "The woman was surprised. 'You're a Jewish man—why are you asking a Samaritan woman for water?' (Jews and Samaritans had nothing to do with each other.)"
    },
    "10": {
      "L": "Jesus answered and said to her: 'If you knew the gift of God and who it is who says to you, Give me a drink, you would have asked him and he would have given you living water.'",
      "M": "Jesus answered her, 'If you knew the gift of God and who it is that asks you for a drink, you would have asked him and he would have given you living water.'",
      "T": "Jesus replied, 'If you only knew what God's gift is—and who is asking you for water—you would have asked him, and he would have given you living water.'"
    },
    "11": {
      "L": "The woman says to him: 'Lord, you have no bucket and the well is deep. Where then do you get this living water?'",
      "M": "'Sir,' the woman said, 'you have nothing to draw with and the well is deep. Where can you get this living water?'",
      "T": "'Sir,' the woman said, 'you don't even have a bucket, and this well is deep. Where would you get this living water from?'"
    },
    "12": {
      "L": "'Are you greater than our father Jacob, who gave us the well and himself drank from it, and his sons, and his livestock?'",
      "M": "'Are you greater than our father Jacob, who gave us the well and drank from it himself, as did also his sons and his livestock?'",
      "T": "'Are you greater than our ancestor Jacob, who dug this well and drank from it himself, along with his sons and his flocks?'"
    },
    "13": {
      "L": "Jesus answered and said to her: 'Everyone who drinks of this water will thirst again;'",
      "M": "Jesus answered, 'Everyone who drinks this water will be thirsty again,'",
      "T": "Jesus replied, 'Anyone who drinks this water will be thirsty again.'"
    },
    "14": {
      "L": "'but whoever drinks of the water that I will give him will never be thirsty again—ever. But the water that I will give him will become in him a spring of water welling up into eternal life.'",
      "M": "'but whoever drinks the water I give them will never thirst. Indeed, the water I give them will become in them a spring of water welling up to eternal life.'",
      "T": "'But whoever drinks the water I give will never be thirsty again. The water I give becomes a perpetual spring within them, gushing up into eternal life.'"
    },
    "15": {
      "L": "The woman says to him: 'Lord, give me this water, so that I may not thirst, nor come here to draw.'",
      "M": "The woman said to him, 'Sir, give me this water so that I won't get thirsty and have to keep coming here to draw water.'",
      "T": "'Please give me this water!' the woman said. 'Then I won't be thirsty anymore, and I won't have to keep coming all the way out here!'"
    },
    "16": {
      "L": "He says to her: 'Go, call your husband and come here.'",
      "M": "He told her, 'Go, call your husband and come back.'",
      "T": "'Go get your husband,' Jesus told her, 'and come back.'"
    },
    "17": {
      "L": "The woman answered and said: 'I have no husband.' Jesus says to her: 'Rightly you said: I have no husband;'",
      "M": "'I have no husband,' she replied. Jesus said to her, 'You are right when you say you have no husband.'",
      "T": "'I don't have a husband,' she replied. Jesus said, 'You're right—you have no husband.'"
    },
    "18": {
      "L": "'for you have had five husbands, and the one you have now is not your husband. This you have said truly.'",
      "M": "'The fact is, you have had five husbands, and the man you now have is not your husband. What you have just said is quite true.'",
      "T": "'The truth is, you've had five husbands, and the man you're with now is not your husband. You were honest about that.'"
    },
    "19": {
      "L": "The woman says to him: 'Lord, I see that you are a prophet.'",
      "M": "'Sir,' the woman said, 'I can see that you are a prophet.'",
      "T": "'Sir,' the woman said, 'I can tell you are a prophet.'"
    },
    "20": {
      "L": "'Our fathers worshiped on this mountain; and you say that in Jerusalem is the place where men must worship.'",
      "M": "'Our ancestors worshiped on this mountain, but you Jews claim that the place where we must worship is in Jerusalem.'",
      "T": "'Our ancestors worshiped God on this mountain, but you Jews say Jerusalem is the only proper place to worship.'"
    },
    "21": {
      "L": "Jesus says to her: 'Believe me, woman, an hour is coming when you will worship the Father neither on this mountain nor in Jerusalem.'",
      "M": "'Woman,' Jesus replied, 'believe me, a time is coming when you will worship the Father neither on this mountain nor in Jerusalem.'",
      "T": "'Believe me,' Jesus told her, 'the time is coming when it won't matter whether you worship the Father on this mountain or in Jerusalem.'"
    },
    "22": {
      "L": "'You worship what you do not know; we worship what we know, because salvation is from the Jews.'",
      "M": "'You Samaritans worship what you do not know; we worship what we do know, for salvation is from the Jews.'",
      "T": "'You Samaritans worship something you don't fully understand. We Jews know what we worship, because salvation comes through the Jewish people.'"
    },
    "23": {
      "L": "'But an hour is coming, and now is, when the true worshipers will worship the Father in spirit and truth, for indeed the Father seeks such people as his worshipers.'",
      "M": "'Yet a time is coming and has now come when the true worshipers will worship the Father in the Spirit and in truth, for they are the kind of worshipers the Father seeks.'",
      "T": "'But the time is coming—in fact it has already arrived—when true worshipers will worship the Father in spirit and truth. The Father is actively looking for such worshipers.'"
    },
    "24": {
      "L": "'God is spirit, and his worshipers must worship in spirit and truth.'",
      "M": "'God is spirit, and his worshipers must worship in the Spirit and in truth.'",
      "T": "'God is spirit, and those who worship him must do so genuinely, from the inside out.'"
    },
    "25": {
      "L": "The woman says to him: 'I know that Messiah is coming'—the one called Christ—'when that one comes, he will announce all things to us.'",
      "M": "The woman said, 'I know that Messiah' (called Christ) 'is coming. When he comes, he will explain everything to us.'",
      "T": "The woman said, 'I know the Messiah is coming—the one they call Christ. When he comes, he will explain everything to us.'"
    },
    "26": {
      "L": "Jesus says to her: 'I who speak to you—I am he.'",
      "M": "Then Jesus declared, 'I, the one speaking to you—I am he.'",
      "T": "Jesus told her plainly, 'I am the Messiah—the one speaking to you right now.'"
    },
    "27": {
      "L": "And at this his disciples came, and they were marveling that he was speaking with a woman. Nevertheless, no one said 'What are you seeking?' or 'Why are you speaking with her?'",
      "M": "Just then his disciples returned and were surprised to find him talking with a woman. But no one asked, 'What do you want?' or 'Why are you talking with her?'",
      "T": "Just then his disciples arrived and were shocked to find him talking with a woman. But none of them dared ask 'Why are you talking to her?' or 'What do you want from her?'"
    },
    "28": {
      "L": "Therefore the woman left her water jar and went into the city and says to the people:",
      "M": "Then, leaving her water jar, the woman went back to the town and said to the people,",
      "T": "The woman left her water jar and hurried into the village, telling everyone,"
    },
    "29": {
      "L": "'Come, see a man who told me everything I ever did. Could this be the Christ?'",
      "M": "'Come, see a man who told me everything I ever did. Could this be the Messiah?'",
      "T": "'Come and meet a man who knew everything about me! Could he be the Messiah?'"
    },
    "30": {
      "L": "They went out of the city and were coming to him.",
      "M": "They came out of the town and made their way toward him.",
      "T": "The people streamed out of the village to see him."
    },
    "31": {
      "L": "In the meantime the disciples were urging him, saying: 'Rabbi, eat.'",
      "M": "Meanwhile his disciples urged him, 'Rabbi, eat something.'",
      "T": "Meanwhile his disciples were urging him, 'Rabbi, have something to eat.'"
    },
    "32": {
      "L": "But he said to them: 'I have food to eat that you do not know about.'",
      "M": "But he said to them, 'I have food to eat that you know nothing about.'",
      "T": "But he told them, 'I have food to eat that you don't know about.'"
    },
    "33": {
      "L": "So the disciples were saying to one another: 'Has anyone brought him something to eat?'",
      "M": "Then his disciples said to each other, 'Could someone have brought him food?'",
      "T": "The disciples whispered to each other, 'Did someone already bring him food?'"
    },
    "34": {
      "L": "Jesus says to them: 'My food is to do the will of him who sent me and to accomplish his work.'",
      "M": "'My food,' said Jesus, 'is to do the will of him who sent me and to finish his work.'",
      "T": "'My food,' Jesus explained, 'is to do what the one who sent me wants, and to complete his work.'"
    },
    "35": {
      "L": "'Do you not say: Four more months and the harvest comes? Behold, I say to you, lift up your eyes and look at the fields—they are already white for harvest.'",
      "M": "'Don't you have a saying, It's still four months until harvest? I tell you, open your eyes and look at the fields! They are ripe for harvest.'",
      "T": "'You have a saying: \"Four more months and then the harvest.\" But look around you—the fields are already ready for harvest!'"
    },
    "36": {
      "L": "'The one who reaps already receives wages and gathers fruit into eternal life, so that the one who sows and the one who reaps may rejoice together.'",
      "M": "'Even now the one who reaps draws a wage and harvests a crop for eternal life, so that the sower and the reaper may be glad together.'",
      "T": "'The harvester is already at work, gathering a crop for eternal life, so that sower and reaper celebrate together.'"
    },
    "37": {
      "L": "'For in this the saying is true: one sows and another reaps.'",
      "M": "'Thus the saying One sows and another reaps is true.'",
      "T": "'The old saying proves itself: one person plants, another harvests.'"
    },
    "38": {
      "L": "'I sent you to reap what you did not labor for. Others have labored, and you have entered into their labor.'",
      "M": "'I sent you to reap what you have not worked for. Others have done the hard work, and you have reaped the benefits of their labor.'",
      "T": "'I am sending you to bring in a harvest you didn't plant. Others did the hard work, and you get to share in the results.'"
    },
    "39": {
      "L": "And from that city many of the Samaritans believed in him because of the word of the woman who testified: 'He told me everything I ever did.'",
      "M": "Many of the Samaritans from that town believed in him because of the woman's testimony, 'He told me everything I ever did.'",
      "T": "Many Samaritans from that village believed in Jesus because of the woman's testimony: 'He told me everything I ever did.'"
    },
    "40": {
      "L": "So when the Samaritans came to him, they were asking him to remain with them; and he remained there two days.",
      "M": "So when the Samaritans came to him, they urged him to stay with them, and he stayed two days.",
      "T": "When the Samaritans arrived, they begged him to stay, and he stayed for two days."
    },
    "41": {
      "L": "And many more believed because of his word,",
      "M": "And because of his words many more became believers.",
      "T": "And many more believed because of what he personally said to them."
    },
    "42": {
      "L": "and they were saying to the woman: 'We no longer believe because of your speech, for we ourselves have heard, and we know that this one is truly the Savior of the world.'",
      "M": "They said to the woman, 'We no longer believe just because of what you said; now we have heard for ourselves, and we know that this man really is the Savior of the world.'",
      "T": "They told the woman, 'We don't believe just because of what you told us—now we've heard him ourselves, and we know this is truly the Savior of the world.'"
    },
    "43": {
      "L": "And after the two days he went out from there into Galilee.",
      "M": "After the two days he left for Galilee.",
      "T": "After those two days Jesus continued on to Galilee."
    },
    "44": {
      "L": "For Jesus himself testified that a prophet has no honor in his own homeland.",
      "M": "(Now Jesus himself had pointed out that a prophet has no honor in his own country.)",
      "T": "Jesus himself had said that a prophet is not honored in his own hometown."
    },
    "45": {
      "L": "So when he came into Galilee, the Galileans received him, having seen all that he did in Jerusalem at the feast—for they also had gone to the feast.",
      "M": "When he arrived in Galilee, the Galileans welcomed him. They had seen all that he had done in Jerusalem at the Passover Festival, for they also had been there.",
      "T": "When he arrived in Galilee, the people welcomed him warmly, for they had seen everything he did at the Passover festival in Jerusalem—they had been there themselves."
    },
    "46": {
      "L": "So he came again to Cana of Galilee, where he had made the water wine. And there was a certain royal official whose son was ill in Capernaum.",
      "M": "Once more he visited Cana in Galilee, where he had turned the water into wine. And there was a certain royal official whose son lay sick at Capernaum.",
      "T": "Jesus returned to Cana in Galilee, where he had turned water into wine. A government official whose son was ill in Capernaum heard that Jesus had arrived in Galilee."
    },
    "47": {
      "L": "When this one heard that Jesus had come from Judea into Galilee, he went to him and was asking him to come down and heal his son, for he was about to die.",
      "M": "When this man heard that Jesus had arrived in Galilee from Judea, he went to him and begged him to come and heal his son, who was close to death.",
      "T": "He went to Jesus and begged him to come to Capernaum and heal his son, who was near death."
    },
    "48": {
      "L": "Therefore Jesus said to him: 'Unless you see signs and wonders, you will not believe.'",
      "M": "'Unless you people see signs and wonders,' Jesus told him, 'you will never believe.'",
      "T": "Jesus responded, 'Will you people never believe unless you see miraculous signs and wonders?'"
    },
    "49": {
      "L": "The royal official says to him: 'Lord, come down before my child dies.'",
      "M": "The royal official said, 'Sir, come down before my child dies.'",
      "T": "'Lord, please come before my child dies!' the official pleaded."
    },
    "50": {
      "L": "Jesus says to him: 'Go; your son lives.' The man believed the word that Jesus spoke to him and was going.",
      "M": "'Go,' Jesus replied, 'your son will live.' The man took Jesus at his word and departed.",
      "T": "Jesus told him, 'Go home. Your son is going to be all right.' The man believed what Jesus said and started home."
    },
    "51": {
      "L": "And already as he was going down, his servants met him saying that his son was alive.",
      "M": "While he was still on the way, his servants met him with the news that his boy was living.",
      "T": "While he was still on his way home, his servants met him with the news: 'Your son is alive!'"
    },
    "52": {
      "L": "So he inquired of them the hour at which he had begun to get better. And they said to him: 'Yesterday at the seventh hour the fever left him.'",
      "M": "When he inquired as to the time when his son got better, they said to him, 'Yesterday at one in the afternoon the fever left him.'",
      "T": "He asked them what time his son had begun to recover. 'The fever left him yesterday at one in the afternoon,' they told him."
    },
    "53": {
      "L": "Then the father knew that it was at that hour in which Jesus said to him: 'Your son lives.' And he himself believed, and his whole household.",
      "M": "Then the father realized that this was the exact time at which Jesus had said to him, 'Your son will live.' So he and his whole household believed.",
      "T": "The father realized that was exactly when Jesus had said, 'Your son is going to live.' And he and all his household believed."
    },
    "54": {
      "L": "This again was the second sign that Jesus did, having come from Judea into Galilee.",
      "M": "This was the second sign Jesus performed after coming from Judea to Galilee.",
      "T": "This was the second miraculous sign Jesus performed after coming to Galilee from Judea."
    }
  },

  "5": {
    "1": {
      "L": "After these things there was a feast of the Jews, and Jesus went up to Jerusalem.",
      "M": "Some time later, Jesus went up to Jerusalem for one of the Jewish festivals.",
      "T": "Some time after this, Jesus went to Jerusalem for one of the Jewish religious festivals."
    },
    "2": {
      "L": "Now there is in Jerusalem by the Sheep Gate a pool, called in Hebrew Bethesda, having five porticoes.",
      "M": "Now there is in Jerusalem near the Sheep Gate a pool, which in Aramaic is called Bethesda and which is surrounded by five covered colonnades.",
      "T": "Inside Jerusalem, near the Sheep Gate, there is a pool called Bethesda in Aramaic, surrounded by five covered porches."
    },
    "3": {
      "L": "In these lay a multitude of the sick—blind, lame, and paralyzed—waiting for the moving of the water.",
      "M": "Here a great number of disabled people used to lie—the blind, the lame, the paralyzed.",
      "T": "Crowds of sick people lay there—the blind, the crippled, the paralyzed."
    },
    "5": {
      "L": "Now a certain man was there who had been in his infirmity for thirty-eight years.",
      "M": "One who was there had been an invalid for thirty-eight years.",
      "T": "One of the men lying there had been sick for thirty-eight years."
    },
    "6": {
      "L": "When Jesus saw him lying there and knew that he had already been in this condition a long time, he says to him: 'Do you want to be made well?'",
      "M": "When Jesus saw him lying there and learned that he had been in this condition for a long time, he asked him, 'Do you want to get well?'",
      "T": "Jesus saw him lying there and knew how long he had been suffering, so he asked, 'Would you like to be healed?'"
    },
    "7": {
      "L": "The sick man answered him: 'Lord, I have no one to put me into the pool when the water is stirred up; but while I am coming, another steps down before me.'",
      "M": "'Sir,' the invalid replied, 'I have no one to help me into the pool when the water is stirred. While I am trying to get in, someone else goes down ahead of me.'",
      "T": "'Sir,' he replied, 'I have no one to help me into the water when it stirs. By the time I try to get in, someone else always gets there first.'"
    },
    "8": {
      "L": "Jesus says to him: 'Rise, take up your mat and walk.'",
      "M": "Then Jesus said to him, 'Get up! Pick up your mat and walk.'",
      "T": "Jesus told him, 'Stand up, pick up your mat, and walk!'"
    },
    "9": {
      "L": "And immediately the man became well, and he took up his mat and was walking. Now that day was a Sabbath.",
      "M": "At once the man was cured; he picked up his mat and walked. The day on which this took place was a Sabbath.",
      "T": "The man was instantly healed. He rolled up his mat and started walking. The day this happened was the Sabbath."
    },
    "10": {
      "L": "Therefore the Jews were saying to the man who had been healed: 'It is the Sabbath, and it is not lawful for you to carry your mat.'",
      "M": "So the Jewish leaders said to the man who had been healed, 'It is the Sabbath; the law forbids you to carry your mat.'",
      "T": "The Jewish leaders confronted the man: 'You can't carry your mat on the Sabbath—that's against the Law!'"
    },
    "11": {
      "L": "But he answered them: 'The one who made me well—that one said to me: Take up your mat and walk.'",
      "M": "But he replied, 'The man who made me well said to me, Pick up your mat and walk.'",
      "T": "He answered, 'The man who healed me told me to pick up my mat and walk.'"
    },
    "12": {
      "L": "They asked him: 'Who is the man who said to you, Take up your mat and walk?'",
      "M": "So they asked him, 'Who is this fellow who told you to pick it up and walk?'",
      "T": "'Who told you to do that?' they demanded."
    },
    "13": {
      "L": "Now the one who had been healed did not know who it was, for Jesus had slipped away, there being a crowd in the place.",
      "M": "The man who was healed had no idea who it was, for Jesus had slipped away into the crowd that was there.",
      "T": "The healed man didn't know, because Jesus had quietly disappeared into the crowd."
    },
    "14": {
      "L": "After these things Jesus finds him in the temple and said to him: 'Behold, you have become well; sin no more, so that nothing worse may happen to you.'",
      "M": "Later Jesus found him at the temple and said to him, 'See, you are well again. Stop sinning or something worse may happen to you.'",
      "T": "Later Jesus found the man in the temple and warned him, 'You have been made well—stop sinning, or something worse may happen to you.'"
    },
    "15": {
      "L": "The man went away and told the Jews that Jesus was the one who had made him well.",
      "M": "The man went away and told the Jewish leaders that it was Jesus who had made him well.",
      "T": "The man went and told the Jewish leaders that it was Jesus who had healed him."
    },
    "16": {
      "L": "And because of this the Jews were persecuting Jesus, because he was doing these things on the Sabbath.",
      "M": "So, because Jesus was doing these things on the Sabbath, the Jewish leaders began to persecute him.",
      "T": "So the Jewish leaders began harassing Jesus for healing on the Sabbath."
    },
    "17": {
      "L": "But Jesus answered them: 'My Father is working until now, and I also am working.'",
      "M": "In his defense Jesus said to them, 'My Father is always at his work to this very day, and I too am working.'",
      "T": "Jesus replied, 'My Father never stops working, and so I keep working too.'"
    },
    "18": {
      "L": "Therefore the Jews were seeking all the more to kill him, because not only was he breaking the Sabbath, but he was also calling God his own Father, making himself equal to God.",
      "M": "For this reason they tried all the more to kill him; not only was he breaking the Sabbath, but he was even calling God his own Father, making himself equal with God.",
      "T": "This made the Jewish leaders even more determined to kill him—not just for breaking the Sabbath, but for calling God his own Father, making himself equal with God."
    },
    "19": {
      "L": "Therefore Jesus answered and was saying to them: 'Truly, truly I say to you, the Son can do nothing on his own—only what he sees the Father doing. For whatever he does, these things the Son also does likewise.'",
      "M": "Jesus gave them this answer: 'Truly, truly, I tell you, the Son can do nothing by himself; he can do only what he sees his Father doing, because whatever the Father does the Son also does.'",
      "T": "Jesus replied, 'I tell you the truth: the Son can do nothing on his own—only what he sees the Father doing. Whatever the Father does, the Son does as well.'"
    },
    "20": {
      "L": "'For the Father loves the Son and shows him all that he himself is doing; and greater works than these he will show him, so that you will be amazed.'",
      "M": "'For the Father loves the Son and shows him all he does. Yes, and he will show him even greater works than these, so that you will be amazed.'",
      "T": "'The Father loves the Son and shows him everything he does. And he will show him even greater things, so that you will be truly astonished.'"
    },
    "21": {
      "L": "'For just as the Father raises the dead and gives them life, so also the Son gives life to whom he wills.'",
      "M": "'For just as the Father raises the dead and gives them life, even so the Son gives life to whom he is pleased to give it.'",
      "T": "'Just as the Father raises the dead and gives them life, the Son also gives life to anyone he chooses.'"
    },
    "22": {
      "L": "'For the Father judges no one, but has given all judgment to the Son,'",
      "M": "'Moreover, the Father judges no one, but has entrusted all judgment to the Son,'",
      "T": "'The Father does not judge anyone—he has handed all judgment over to the Son.'"
    },
    "23": {
      "L": "'so that all may honor the Son just as they honor the Father. The one who does not honor the Son does not honor the Father who sent him.'",
      "M": "'that all may honor the Son just as they honor the Father. Whoever does not honor the Son does not honor the Father, who sent him.'",
      "T": "'This is so that everyone will honor the Son just as they honor the Father. Anyone who refuses to honor the Son is refusing to honor the Father who sent him.'"
    },
    "24": {
      "L": "'Truly, truly I say to you, the one who hears my word and believes him who sent me has eternal life and does not come into judgment, but has passed out of death into life.'",
      "M": "'Truly, truly, I tell you, whoever hears my word and believes him who sent me has eternal life and will not be judged but has crossed over from death to life.'",
      "T": "'I tell you the absolute truth: those who hear what I say and trust the one who sent me already possess eternal life—they have moved from death into life and will never face condemnation.'"
    },
    "25": {
      "L": "'Truly, truly I say to you, an hour is coming, and now is, when the dead will hear the voice of the Son of God, and those who hear will live.'",
      "M": "'Truly, truly, I tell you, a time is coming and has now come when the dead will hear the voice of the Son of God and those who hear will live.'",
      "T": "'I tell you the truth: the time is coming—and has already arrived—when the dead will hear the voice of the Son of God, and those who hear will come alive.'"
    },
    "26": {
      "L": "'For just as the Father has life in himself, so also he has granted to the Son to have life in himself.'",
      "M": "'For as the Father has life in himself, so he has granted the Son also to have life in himself.'",
      "T": "'The Father has life within himself, and he has granted the Son to have life within himself as well.'"
    },
    "27": {
      "L": "'And he has given him authority to execute judgment, because he is the Son of Man.'",
      "M": "'And he has given him authority to judge because he is the Son of Man.'",
      "T": "'And he has given him authority to judge, because he is the Son of Man.'"
    },
    "28": {
      "L": "'Do not marvel at this, for an hour is coming in which all who are in the tombs will hear his voice'",
      "M": "'Do not be amazed at this, for a time is coming when all who are in their graves will hear his voice'",
      "T": "'Don't be surprised by this. The time is coming when all the dead in their graves will hear his voice'"
    },
    "29": {
      "L": "'and come out—those who have done good to a resurrection of life, and those who have practiced evil to a resurrection of judgment.'",
      "M": "'and come out—those who have done what is good will rise to live, and those who have done what is evil will rise to be condemned.'",
      "T": "'and come out—those who did good will rise to life, and those who did evil will rise to face judgment.'"
    },
    "30": {
      "L": "'I can do nothing on my own; as I hear, I judge; and my judgment is righteous, because I do not seek my own will but the will of him who sent me.'",
      "M": "'By myself I can do nothing; I judge only as I hear, and my judgment is just, for I seek not to please myself but him who sent me.'",
      "T": "'I cannot act on my own. I judge only on the basis of what I hear from the Father, and my judgment is always right because I am not trying to please myself, but the one who sent me.'"
    },
    "31": {
      "L": "'If I testify about myself, my testimony is not valid.'",
      "M": "'If I testify about myself, my testimony is not true.'",
      "T": "'If I were the only one testifying on my own behalf, my testimony wouldn't carry much weight.'"
    },
    "32": {
      "L": "'There is another who testifies about me, and I know that the testimony he gives about me is true.'",
      "M": "'There is another who testifies in my favor, and I know that his testimony about me is true.'",
      "T": "'But there is another who testifies on my behalf, and I know his testimony about me is reliable.'"
    },
    "33": {
      "L": "'You have sent to John, and he has testified to the truth.'",
      "M": "'You have sent to John and he has testified to the truth.'",
      "T": "'You yourselves sent a delegation to John, and he testified truthfully about me.'"
    },
    "34": {
      "L": "'But the testimony I receive is not from man; but I say these things that you may be saved.'",
      "M": "'Not that I accept human testimony; but I mention it that you may be saved.'",
      "T": "'Not that I need a human witness—but I bring this up so that you might be rescued.'"
    },
    "35": {
      "L": "'That one was the burning and shining lamp, and you were willing for a time to rejoice in his light.'",
      "M": "'John was a lamp that burned and gave light, and you chose for a time to enjoy his light.'",
      "T": "'John was a lamp burning brightly, and for a while you were happy to enjoy the light he gave.'"
    },
    "36": {
      "L": "'But the testimony I have is greater than John's; for the works that the Father has given me to accomplish—the very works that I am doing—testify about me that the Father has sent me.'",
      "M": "'I have testimony weightier than that of John. For the works that the Father has given me to finish—the very works I am doing—testify that the Father has sent me.'",
      "T": "'But I have a testimony that is greater than John's—the works the Father gave me to complete. The very miracles I am doing testify that the Father sent me.'"
    },
    "37": {
      "L": "'And the Father who sent me has himself testified about me. You have neither heard his voice at any time, nor seen his form,'",
      "M": "'And the Father who sent me has himself testified concerning me. You have never heard his voice nor seen his form,'",
      "T": "'And the Father who sent me has himself testified about me. You have never heard his voice or seen his face,'"
    },
    "38": {
      "L": "'and you do not have his word remaining in you, because the one he sent—him you do not believe.'",
      "M": "'nor does his word dwell in you, for you do not believe the one he sent.'",
      "T": "'and his word does not live in you, because you refuse to believe the one he sent.'"
    },
    "39": {
      "L": "'You search the scriptures because you think in them you have eternal life; and it is these that testify about me;'",
      "M": "'You study the Scriptures diligently because you think that in them you have eternal life. These are the very Scriptures that testify about me,'",
      "T": "'You pour over the scriptures because you think eternal life is in them—yet those very scriptures point to me!'"
    },
    "40": {
      "L": "'and yet you are not willing to come to me that you may have life.'",
      "M": "'yet you refuse to come to me to have life.'",
      "T": "'And still you refuse to come to me to actually receive that life.'"
    },
    "41": {
      "L": "'I do not receive glory from men;'",
      "M": "'I do not accept glory from human beings,'",
      "T": "'I don't need praise from people—'"
    },
    "42": {
      "L": "'but I know you—that you do not have the love of God in you.'",
      "M": "'but I know you. I know that you do not have the love of God in your hearts.'",
      "T": "'but I know what you are really like—the love of God is not in you.'"
    },
    "43": {
      "L": "'I have come in the name of my Father, and you do not receive me; if another comes in his own name, that one you will receive.'",
      "M": "'I have come in my Father's name, and you do not accept me; but if someone else comes in his own name, you will accept him.'",
      "T": "'I came representing my Father, and you rejected me. But when someone comes representing only himself, you'll accept him readily.'"
    },
    "44": {
      "L": "'How can you believe, when you receive glory from one another and do not seek the glory that comes from the only God?'",
      "M": "'How can you believe since you accept glory from one another but do not seek the glory that comes from the only God?'",
      "T": "'How could you possibly believe when all you care about is what other people think of you, and you never seek the honor that comes from the only God?'"
    },
    "45": {
      "L": "'Do not think that I will accuse you before the Father; the one who accuses you is Moses, in whom you have put your hope.'",
      "M": "'But do not think I will accuse you before the Father. Your accuser is Moses, on whom your hopes are set.'",
      "T": "'Don't imagine that I will accuse you before the Father. Moses will be your accuser—the very Moses you claim to trust.'"
    },
    "46": {
      "L": "'For if you believed Moses, you would believe me; for he wrote about me.'",
      "M": "'If you believed Moses, you would believe me, for he wrote about me.'",
      "T": "'If you actually believed Moses, you would believe me—because Moses wrote about me.'"
    },
    "47": {
      "L": "'But if you do not believe his writings, how will you believe my words?'",
      "M": "'But since you do not believe what he wrote, how are you going to believe what I say?'",
      "T": "'But if you don't believe what Moses wrote, how will you ever believe what I say?'"
    }
  }
}

# ── Write output ───────────────────────────────────────────────────────────
def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'john')
    merge_tier(data, JOHN, key)
    save(tier, 'john', data)

print('\nJohn 1–5 written to all three tiers.')
print('Chapters covered:', sorted(JOHN.keys(), key=int))
