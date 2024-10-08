import random
import tweepy
import os
import requests

API_KEY = 'placeholder'
API_SECRET_KEY = 'placeholder'
access_token = 'placeholder'
access_token_secret = 'placeholder'
bearer_token = 'placeholder'
consumer_key = 'placeholder'
consumer_secret = 'placeholder'

        # Authenticate to Twitter using Client for v2 API
client = tweepy.Client(
    bearer_token = bearer_token,
    consumer_key = API_KEY,
    consumer_secret = API_SECRET_KEY,
    access_token = access_token,
    access_token_secret = access_token_secret
)
temp_filename = '/tmp/temp_media.gif'

#
# Authenticate to Twitter using OAuth1UserHandler for media upload (v1.1)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, access_token,access_token_secret)
api = tweepy.API(auth)



def SW_gif_post(event,context):
    gif_dict = {
        "1_eP1_yoda_senseMuchFear.gif": "I sense much fear in you. -Yoda",
        "ahsoka-v-maul-cw-s7.gif": "lol",
        "anakin-ep1-no-one-kill-jedi.gif": "no one?",
        "bad-feeling-kenobi.gif": "bad feeling about this...",
        "bad-feeling-luke.gif": "bad feeling about this...",
        "begun-clone-wars-yoda.gif": "*Queue Clone Wars intro music*",
        "don't-like-sand.gif": "I don't like sand. It's corase, and rough, and irritating... and it gets everywhere",
        "dooku-looking-forward.gif": "same",
        "empire-reorganized.gif": "so this is how liberty dies...?",
        "execute-order-66.gif": "execute order 66",
        "force-ghost-luke.gif": "W force ghost",
        "fun-begins.gif": "this is where the fun begins",
        "good-soldiers-starwars.gif": "good soldiers follow orders",
        "half-ship.gif": "xD",
        "high-ground.gif": "don't underestimate his power",
        "i-love-democracy.gif": "i love democracy",
        "kenobi-bar-ep2.gif": "you don't want to sell me deathsticks",
        "lack-of-faith.gif": "amazing scene",
        "maul-cw-s7.gif": "Maul",
        "maul-death.gif": "Maul death",
        "more-powerful-ben-kenobi.gif": "Ben Kenobi",
        "name-no-meaning-vader-ep6.gif": "Anakin",
        "not-how-force-works.gif": "lol",
        "obiwan-brother.gif": ":(",
        "order66-cw.gif": "Execute order 66",
        "palpatine-ep5.gif": "Palpatine",
        "pod-racing.gif": "Now this is pod racing",
        "power-dark-side.gif": "Darth Vader",
        "q_Ahsoka_ezra.gif": "Jabba the Hutt",
        "q_Ep1_itsWorking.gif": "Ani",
        "q_Ep2_begunclonewar.gif": "Yoda",
        "q_Ep2_simplemantryingto.gif": "Jango Fett",
        "q_Ep3_anakin_wegotemr2.gif": "W R2 moment",
        "q_Ep3_flyingisfordroids.gif": "Obi-Wan Kenobi",
        "q_Ep3_souncivilized.gif": "Obi-Wan Kenobi",
        "q_Ep5_Yoda_mine.gif": "Yoda",
        "q_Ep5_leia_goback.gif": "Leia",
        "q_Ep5_vader.gif": "Darth Vader",
        "q_Ep5_vaderVlukesurpirses.gif": "Luke v. Vader",
        "q_Ep6_Ewok_Grr.gif": "Ewok",
        "q_Ep6_Sheilddeactive.gif": "Return of the Jedi",
        "q_Ep6_Vader_hopeso.gif": "Darth Vader",
        "q_Ep6_c3p0.gif": "Return of the Jedi",
        "q_Ep6_doublefforts.gif": "Return of the Jedi",
        "q_Ep6_freeusordie.gif": "Luke Skywalker",
        "q_Ep6_leia_freeze.gif": "Leia",
        "q_Ep6_leia_someonewholovesyou.gif": "Han + Leia",
        "q_Ep6_monthmaunprotected.gif": "Return of the Jedi",
        "q_Ep6_yoda_luke_Forceinfamily.gif": "Yoda",
        "q_Ep7_c3p0missyou.gif": "C3PO",
        "q_Ep7_finn_escape.gif": "Finn",
        "q_Ep7_finn_usetheforce.gif": "that's not how the force works",
        "q_Ep7_nothowtheforceworks.gif": "that's not how the force works",
        "q_ahsoka_Forceanakin.gif": "Anakin Skywalker",
        "q_ahsoka_ahsoka.gif": "Ahsoka",
        "q_ahsoka_ahsoka2.gif": "Ahsoka",
        "q_ahsoka_ahsoka3.gif": "Ahsoka",
        "q_ahsoka_ahsoka4.gif": "Ahsoka",
        "q_ahsoka_anakin.gif": "Sky guy",
        "q_ahsoka_cw.gif": "Snips",
        "q_ahsoka_droid.gif": "Ahsoka",
        "q_ahsoka_droid2.gif": "Ahsoka",
        "q_ahsoka_droid3.gif": "Ahsoka",
        "q_ahsoka_droid4.gif": "Ahsoka",
        "q_ahsoka_droid5.gif": "Ahsoka",
        "q_ahsoka_ezra2.gif": "Jabba the Hutt",
        "q_ahsoka_ezra3.gif": "Jabba",
        "q_ahsoka_ezra4.gif": "is that Jabba?",
        "q_ahsoka_flashb.gif": "Anakin Skywalker",
        "q_ahsoka_hera.gif": "Hera",
        "q_ahsoka_hera2.gif": "Hera",
        "q_ahsoka_hera_mtfbwy.gif": "May the Force be with you",
        "q_ahsoka_nightsiste.gif": "Ahsoka",
        "q_ahsoka_sabine.gif": "Sabine",
        "q_ahsoka_sabine2.gif": "Sabine",
        "q_ahsoka_sabine3.gif": "Padawan",
        "q_ahsoka_sabine4.gif": "Sabine",
        "q_ahsoka_sabine5.gif": "Sabine",
        "q_ahsoka_sith.gif": "Going somewhere?",
        "q_ahsoka_sith2.gif": "hmm",
        "q_ahsoka_sith3.gif": "Ahsoka",
        "q_ahsoka_sith4.gif": "Jedi?",
        "q_ahsoka_thrawn.gif": "Thrawn",
        "q_ahsoka_thrawn2.gif": "Thrawn",
        "q_ahsoka_thrawn3.gif": "Thrawn",
        "q_ahsoka_thrawn4.gif": "Thrawn",
        "q_ahsoka_thrawn5.gif": "Thrawn",
        "q_ahsoka_thrawn6.gif": "Grand Admiral Thraw",
        "q_ahsoka_thrawn7.gif": "Thrawn",
        "q_ahsoka_thrawn_fortheempire.gif": "For the empire",
        "q_ahsoka_thrawn_longliveempire.gif": "Long live the empire",
        "q_ahsoka_wbw.gif": "Ahsoka",
        "q_ahsoka_wbw2.gif": "World between worlds",
        "q_ep1_3p0PartsShowing.gif": "lol",
        "q_ep1_AniYoureAJediToo.gif": "wholesome scene",
        "q_ep1_ahVictory.gif": "Ah, victory",
        "q_ep1_anakinMeetObiwan.gif": "off to a great start",
        "q_ep1_angel.gif": "rizz",
        "q_ep1_biggerFish.gif": "there's always a bigger fish",
        "q_ep1_c3p0JarJarlittleOdd.gif": "same",
        "q_ep1_c3p0WhereIsEverybody.gif": "C-3PO",
        "q_ep1_council_mtfbwy.gif": "always...",
        "q_ep1_doesntCompute.gif": "doesn't compute",
        "q_ep1_endingPEACE.gif": "Peace!",
        "q_ep1_endingYouwillbejediOBiwan.gif": "The Phantom Menace",
        "q_ep1_gunray.gif": "The Phantom Menace",
        "q_ep1_jarjar.gif": "The Phantom Menace",
        "q_ep1_jarjar_3.gif": "a Sith Lord?",
        "q_ep1_jarjar_4.gif": "Jar Jar",
        "q_ep1_jarjar_5.gif": "wise words",
        "q_ep1_jarjar_7.gif": "The Phantom Menace",
        "q_ep1_jarjar_8.gif": "The Phantom Menace",
        "q_ep1_mass.gif": "The Phantom Menace",
        "q_ep1_mass_!.gif": "I have a bad feeling about this",
        "q_ep1_mass_2.gif": "The Phantom Menace",
        "q_ep1_mass_3.gif": "The Phantom Menace",
        "q_ep1_mass_4.gif": "The Phantom Menace",
        "q_ep1_mass_5.gif": "Return of the King",
        "q_ep1_momSaidPeopleDontHelp.gif": "The Phantom Menace",
        "q_ep1_no1killJedi.gif": "No one?",
        "q_ep1_nowthisispodracing.gif": "Now this is podracing!",
        "q_ep1_padmeANAKIN.gif": "She is 14, he is 9.",
        "q_ep1_personNameIsAnakin.gif": "I'm a person and my name is Anakin",
        "q_ep1_podracing.gif": "The Phantom Menace",
        "q_ep1_podracing_1.gif": "The Phantom Menace",
        "q_ep1_quigon.gif": "The Phantom Menace",
        "q_ep1_tryspinning_goodtrick.gif": "I'll try spinning. That's a good trick!",
        "q_ep1_watchcareerwithgreatinterest.gif": "Foreshadowing...",
        "q_ep1_yippe.gif": "The Phantom Menace",
        "q_ep1_yoda_FearPathDarkside.gif": "The Phantom Menace",
        "q_ep1_yoda_HardToSeeDarkSide.gif": "The Phantom Menace",
        "q_ep2_anakin_badfeelingaboutthis.gif": "I have a bad feeling about this...",
        "q_ep2_anakin_dontworrywehaver2.gif": "Attack of the Clones",
        "q_ep2_anakin_obiwangrumpyifcaughtme.gif": "Attack of the Clones",
        "q_ep2_anakin_youreexactlyasirememberinmydreams.gif": "Rizz",
        "q_ep2_boba_yep.gif": "Attack of the Clones",
        "q_ep2_c3p0_droid_programmedforetiquette.gif": "Attack of the Clones",
        "q_ep2_c3p0confused.gif": "Attack of the Clones",
        "q_ep2_c3p0terriblysorry.gif": "Attack of the Clones",
        "q_ep2_darkSideCloudsEverythingYoda.gif": "Attack of the Clones",
        "q_ep2_dex.gif": "Attack of the Clones",
        "q_ep2_dexHeyOldBuddy.gif": "Hey, old buddy!",
        "q_ep2_dex_whattyaknow.gif": "Whattaya know",
        "q_ep2_diplomaticSolution.gif": "No, I call it aggressive negotiations",
        "q_ep2_dontmindFlyingButSuicide.gif": "Attack of the Clones",
        "q_ep2_dooku_sorryoldfriend.gif": "Attack of the Clones",
        "q_ep2_goHomeRethinkLife.gif": "You don't want to sell my deathsticks...",
        "q_ep2_goodcallyoungpadawan.gif": "Attack of the Clones",
        "q_ep2_iSenseitToo.gif": "Attack of the Clones",
        "q_ep2_idontlikesand.gif": "I don't like sand.",
        "q_ep2_ilovedemocracy.gif": "I love democracy",
        "q_ep2_impossibleToSeeFuture.gif": "Attack of the Clones",
        "q_ep2_jango_alwayspleasuretomeetjedi.gif": "Attack of the Clones",
        "q_ep2_jango_packbags.gif": "Attack of the Clones",
        "q_ep2_kenobi_goodjob.gif": "Attack of the Clones",
        "q_ep2_kenobi_possibly.gif": "Possibly",
        "q_ep2_mace_keepersofPeaceNotSoldiers.gif": "Attack of the Clones",
        "q_ep2_mace_thispartysover.gif": "Attack of the Clones",
        "q_ep2_negotationsNotFailPalpatine.gif": "Attack of the Clones",
        "q_ep2_obiwan.gif": "Attack of the Clones",
        "q_ep2_obiwanAniLittleOnEdge.gif": "Attack of the Clones",
        "q_ep2_obiwanSweatingTakeDeepBreath.gif": "Attack of the Clones",
        "q_ep2_obiwanUseTheForceThink.gif": "Think",
        "q_ep2_obiwanWHAT.gif": "What?",
        "q_ep2_obiwan_goodnews.gif": "Attack of the Clones",
        "q_ep2_obiwan_hateitwhenhedoeshtat.gif": "same",
        "q_ep2_obiwan_kamino.gif": "Attack of the Clones",
        "q_ep2_padme_dontgrowuptoofast.gif": "Attack of the Clones",
        "q_ep2_padme_dontlookatmelikethat.gif": "oof",
        "q_ep2_padme_makingfunofme.gif": "Attack of the Clones",
        "q_ep2_personalFeelings.gif": "Attack of the Clones",
        "q_ep2_rogerroger.gif": "Roger Roger",
        "q_ep2_suchdrag.gif": "Battle of Geonosis",
        "q_ep2_yoda_howembarassing.gif": "Attack of the Clones",
        "q_ep2_yoda_muchtolearnyoustillhave.gif": "Attack of the Clones",
        "q_ep3_Crawl.gif": "Revenge of the Sith",
        "q_ep3_Dooku_twicepridedoublefall.gif": "Twice the pride, double the fall",
        "q_ep3_ExecuteOrder66.gif": "Execute order 66",
        "q_ep3_allegience.gif": "My allegiance is to the Republic, to democracy!",
        "q_ep3_alwaysonthemove.gif": "Always on the move",
        "q_ep3_anakinSoBeautiful.gif": "Revenge of the Sith",
        "q_ep3_badfeelingaboutthis.gif": "I have a bad feeling about this",
        "q_ep3_chosenone.gif": "The chosen one?",
        "q_ep3_doit.gif": "Do it",
        "q_ep3_donttryit.gif": "Don't try it",
        "q_ep3_dookuSenseMuchFear.gif": "Revenge of the Sith",
        "q_ep3_failedYouAnakin.gif": "Revenge of the Sith",
        "q_ep3_fearispathtodarkside.gif": "Revenge of the Sith",
        "q_ep3_forcestronginyou.gif": "Revenge of the Sith",
        "q_ep3_goodbyeOldFriend.gif": "this is the last time they talk before Anakin becomes Darth Vader",
        "q_ep3_grevious.gif": "Revenge of the Sith",
        "q_ep3_happylanding.gif": "another happy landing",
        "q_ep3_heldhostageutapau.gif": "Revenge of the Sith",
        "q_ep3_helpmehelpme.gif": "Revenge of the Sith",
        "q_ep3_highground.gif": "I have the High Ground",
        "q_ep3_intoexile.gif": "Failed, I have",
        "q_ep3_isenseatrap.gif": "Next move? Spring the trap",
        "q_ep3_ishouldnt.gif": "do it",
        "q_ep3_itstreasonthen.gif": "it's treason then",
        "q_ep3_killhim.gif": "kill him now",
        "q_ep3_libertydies.gif": "at least it's not dying because it's sad",
        "q_ep3_lostwill.gif": "i hate it when that happens",
        "q_ep3_mtfbwya.gif": "always",
        "q_ep3_mustrealizedoome.gif": "oh i don't think so",
        "q_ep3_nonono.gif": "Revenge of the Sith",
        "q_ep3_noooo.gif": "Nooooo",
        "q_ep3_nowthatsbetter.gif": "Revenge of the Sith",
        "q_ep3_ohidontthinkso.gif": "Revenge of the Sith",
        "q_ep3_ohitsyou.gif": "Revenge of the Sith",
        "q_ep3_ohthisgoingtobeeasy.gif": "Revenge of the Sith",
        "q_ep3_order66.gif": "Execute order 66",
        "q_ep3_padmeAnakinMustafar.gif": "Revenge of the Sith",
        "q_ep3_palpatine_goodnews.gif": "Revenge of the Sith",
        "q_ep3_patiencerayshield.gif": "Revenge of the Sith",
        "q_ep3_planb.gif": "What about a Plan C?",
        "q_ep3_resolve.gif": "Revenge of the Sith",
        "q_ep3_senatedecidefate.gif": "I am the senate.",
        "q_ep3_shorterthaniexpected.gif": "oof",
        "q_ep3_takeaseat.gif": "Take a seat.",
        "q_ep3_tragedy.gif": "it's not a story the Jedi would tell you",
        "q_ep3_underarrest.gif": "Revenge of the Sith",
        "q_ep3_underestimatemypower.gif": "don't try it",
        "q_ep3_unlimitedPOwer.gif": "Revenge of the Sith",
        "q_ep3_usemyknowledge.gif": "Revenge of the Sith",
        "q_ep3_yodasidious.gif": "Revenge of the Sith",
        "q_ep4_Forceweakminded.gif": "A New Hope",
        "q_ep4_Vader_partrebelalliance.gif": "A New Hope",
        "q_ep4_Vader_passengersalive.gif": "didn't he just slice thru the hallway 5 minutes ago?",
        "q_ep4_ben.gif": "A New Hope",
        "q_ep4_ben_beforeempire.gif": "Ben Kenobi",
        "q_ep4_ben_comeherelittlefriend.gif": "Ben Kenobi",
        "q_ep4_ben_dontseehisid.gif": "Ben Kenobi",
        "q_ep4_ben_fearsomethingterrible.gif": "Ben Kenobi",
        "q_ep4_ben_forcewillbewithyou.gif": "Ben Kenobi",
        "q_ep4_ben_hellothere.gif": "The original 'Hello there'",
        "q_ep4_ben_iknowhimheme.gif": "Ben Kenobi",
        "q_ep4_ben_learnforceluke.gif": "Ben Kenobi",
        "q_ep4_ben_learnthewaysofforce.gif": "Ben Kenobi",
        "q_ep4_ben_oncejediknight.gif": "Ben Kenobi",
        "q_ep4_ben_strikemedown.gif": "Ben Kenobi",
        "q_ep4_c3p0_Regretthis.gif": "Ben Kenobi",
        "q_ep4_c3p0noescapeprincess.gif": "A New Hope",
        "q_ep4_elegantweapon.gif": "A New Hope",
        "q_ep4_han_donteveryonethankme.gif": "A New Hope",
        "q_ep4_han_imhansolo.gif": "Han Solo",
        "q_ep4_han_neverheardofmilleniumfalcon.gif": "Han Solo",
        "q_ep4_han_shipmadekesselrun12parsecs.gif": "Han Solo",
        "q_ep4_han_yahoo.gif": "Han Solo",
        "q_ep4_hologramleia.gif": "Princess Leia",
        "q_ep4_leia_dontknowhoyouare.gif": "Princess Leia",
        "q_ep4_leia_helpmeobiwanekenobi.gif": "Help me, Obi-Wan Kenobi. You're my only hope.",
        "q_ep4_leia_sass.gif": "Princess Leia",
        "q_ep4_leia_senatenotstand.gif": "I am the senate.",
        "q_ep4_leia_shortforastormtrooper.gif": "Princess Leia",
        "q_ep4_luke_badfeelingaboutthis.gif": "I have a very bad feeling about this",
        "q_ep4_luke_fightagainstempire.gif": "Luke Skywalker",
        "q_ep4_luke_force.gif": "Luke Skywalker",
        "q_ep4_luke_foughtinclonewars.gif": "You fought in the Clone Wars?",
        "q_ep4_luke_whoisshebeautiful.gif": "that's your sister",
        "q_ep4_lukebecomejedi.gif": "Luke Skywalker",
        "q_ep4_namenotheardinlongtime.gif": "Ben Kenobi",
        "q_ep4_notdroidsyoulookingfor.gif": "These aren't the droids you're looking for",
        "q_ep4_oncefatherlightsaber.gif": "Ben Kenobi",
        "q_ep4_tarkin_Fearkeeptheminline.gif": "Tarkin",
        "q_ep4_tarkin_crushrebellion.gif": "Tarkin",
        "q_ep4_tarkinandleia.gif": "Tarkin",
        "q_ep4_vader_Transmissionchoke.gif": "Darth Vader",
        "q_ep4_vader_destroyplanetforce.gif": "Darth Vader",
        "q_ep4_vader_facehimalone.gif": "Darth Vader",
        "q_ep4_vader_happenedtoplans.gif": "Darth Vader",
        "q_ep4_vader_lackoffaith.gif": "I find your lack of faith disturbing",
        "q_ep4_vaderwemeetagainatlast.gif": "Darth Vader",
        "q_ep4_wonderifhemeansben.gif": "Darth Vader",
        "q_ep4_wretchedhive.gif": "Mos Eisley",
        "q_ep5_Ben2.gif": "",
        "q_ep5_Vader_Destroyyou.gif": "",
        "q_ep5_Vader_mostimpressive.gif": "",
        "q_ep5_Yoda.gif": "",
        "q_ep5_Yoda_Thatiswhyyoufail.gif": "",
        "q_ep5_Yoda_energysurroundsus.gif": "",
        "q_ep5_ben.gif": "",
        "q_ep5_c3p0_waitforme.gif": "",
        "q_ep5_doordonot.gif": "",
        "q_ep5_han.gif": "",
        "q_ep5_han_punchit.gif": "",
        "q_ep5_han_watchthis.gif": "",
        "q_ep5_lando.gif": "",
        "q_ep5_leia.gif": "",
        "q_ep5_leia_iloveyou.gif": "",
        "q_ep5_leia_vaderwantsusdead.gif": "",
        "q_ep5_luke_nooo.gif": "",
        "q_ep5_lukeforce.gif": "",
        "q_ep5_palpatine.gif": "",
        "q_ep5_palpatine2.gif": "",
        "q_ep5_r2.gif": "",
        "q_ep5_vader_Destiny.gif": "",
        "q_ep5_vader_Failedmelasttime.gif": "",
        "q_ep5_vader_dontfailme.gif": "",
        "q_ep5_vader_iamyourfather.gif": "",
        "q_ep5_xwing.gif": "",
        "q_ep5_yeti.gif": "",
        "q_ep5_yoda_judgemebysize.gif": "",
        "q_ep6_Deathstaronschedule.gif": "",
        "q_ep6_akbar_force.gif": "",
        "q_ep6_badfeeling.gif": "",
        "q_ep6_boba.gif": "",
        "q_ep6_greetingsexaltedone.gif": "",
        "q_ep6_grr.gif": "",
        "q_ep6_han.gif": "",
        "q_ep6_han_gl.gif": "",
        "q_ep6_han_ohgreat.gif": "",
        "q_ep6_luke.gif": "",
        "q_ep6_luke_vaderonthatship.gif": "",
        "q_ep6_palpatine.gif": "",
        "q_ep6_palpatine_compassion.gif": "",
        "q_ep6_trap.gif": "",
        "q_ep7_Rey_jedimindtrick.gif": "",
        "q_ep7_c3p0.gif": "",
        "q_ep7_escapenow_huglater.gif": "",
        "q_ep7_finishwhatstarted.gif": "",
        "q_ep7_finn_phasma.gif": "",
        "q_ep7_finn_poeineedurhelp.gif": "",
        "q_ep7_finn_stormtrooper.gif": "",
        "q_ep7_fn2187.gif": "",
        "q_ep7_galaxycountingonus.gif": "",
        "q_ep7_han.gif": "",
        "q_ep7_han2.gif": "",
        "q_ep7_han_chewiegetready.gif": "",
        "q_ep7_hanstolefalcon.gif": "",
        "q_ep7_kylo.gif": "",
        "q_ep7_kylo_lightsaberbelongstome.gif": "",
        "q_ep7_kylo_show.gif": "",
        "q_ep7_kylo_traitor.gif": "",
        "q_ep7_leia.gif": "",
        "q_ep7_leia_mtfwbwy.gif": "",
        "q_ep7_leia_tellme.gif": "",
        "q_ep7_leiafinn.gif": "",
        "q_ep7_leialuke.gif": "",
        "q_ep7_maz.gif": "",
        "q_ep7_maz2.gif": "",
        "q_ep7_needpilot.gif": "",
        "q_ep7_poe.gif": "",
        "q_ep7_poe_xwing.gif": "",
        "q_ep7_poejacket.gif": "",
        "q_ep7_poetalkfirst.gif": "",
        "q_ep7_programmedfrombirth.gif": "",
        "q_ep7_rey.gif": "",
        "q_ep7_rey_lukemyth.gif": "",
        "q_ep7_rey_withresistance.gif": "",
        "q_ep7_worse.gif": "",
        "q_ep8_bb8.gif": "",
        "q_ep8_salt.gif": "",
        "q_ep8_yoda_greatestteacher.gif": "",
        "q_han_driver.gif": "",
        "q_mando_Exactly_jackblack.gif": "",
        "q_mando_Feelingyouhatedme.gif": "",
        "q_mando_badbaby.gif": "",
        "q_mando_billbur.gif": "",
        "q_mando_bokatan_thisistheway.gif": "",
        "q_mando_dontbebaby.gif": "",
        "q_mando_fly_mtfbwy.gif": "",
        "q_mando_fool.gif": "",
        "q_mando_interesting.gif": "",
        "q_mando_jedi.gif": "",
        "q_mando_karga.gif": "",
        "q_mando_playtimeover.gif": "",
        "q_mando_pogsoup.gif": "",
        "q_mando_thisistheway.gif": "",
        "q_mando_thisistheway2.gif": "",
        "q_mando_tuesdays.gif": "",
        "q_mando_wait.gif": "",
        "q_mando_welcomeback.gif": "",
        "q_mando_yes.gif": "",
        "q_roge1_k2s0.gif": "",
        "q_rogue1_akbar_mtfbwy.gif": "",
        "q_rogue1_backup.gif": "",
        "q_rogue1_explosion.gif": "",
        "q_rogue1_farming.gif": "",
        "q_rogue1_jyn.gif": "",
        "q_rogue1_k2s0.gif": "",
        "q_rogue1_k2s01.gif": "",
        "q_rogue1_krennic.gif": "",
        "q_rogue1_krennic2.gif": "",
        "q_rogue1_myachievement.gif": "",
        "q_rogue1_onewithforce.gif": "",
        "q_rogue1_rebel.gif": "",
        "q_rogue1_rescued.gif": "",
        "q_rogue1_vader.gif": "",
        "q_rogue1_vaderhelpus.gif": "",
        "q_solo_inthislifeforgood.gif": "",
        "q_solo_lando.gif": "",
        "roger-roger.gif": "",
        "rose-cringe-ep8.gif": "",
        "sense-fear-yoda.gif": "",
        "simple-man-trying-to.gif": "",
        "somehow-palpatine-returned.gif": "",
        "take-a-seat.gif": "",
        "the-senate.gif": "",
        "this-is-the-way.gif": "",
        "verge-of-greatness.gif": ""
    }


    # Select a random GIF from the dictionary
    random_key = random.choice(list(gif_dict.keys()))
    gif_url = "https://raw.githubusercontent.com/spencermarshall/StarWarsTwitterPost/main/images/quote-or-meme/" + random_key

    # Temporary file path in AWS Lambda
    temp_filename = '/tmp/temp_media.gif'

    # Download the GIF
    response = requests.get(gif_url)
    if response.status_code == 200:
        # Save the content to the temporary file
        with open(temp_filename, 'wb') as temp_file:
            temp_file.write(response.content)

        # Upload the GIF using Tweepy
        media = api.media_upload(temp_filename)

        # Tweet text
        tweet_text = ""

        # Add hashtags with probabilities
        percDict = {"#StarWars ": 0.25}
        tags = ["#StarWars ", "#swtwt "]
        tagsString = ""
        for tag in tags:
            randomProb = 0.1  # Default probability
            if tag in percDict:
                randomProb = percDict[tag]
            if random.random() < randomProb:
                tagsString += tag

        # Append hashtags to tweet text
        tweet_text += tagsString

        # Post the tweet with the GIF
        client.create_tweet(text=tweet_text, media_ids=[media.media_id])

        # Remove the temporary file after posting the twee t
        os.remove(temp_filename)

        return "Tweet posted successfully!"
    else:
        return "Failed to download GIF."
