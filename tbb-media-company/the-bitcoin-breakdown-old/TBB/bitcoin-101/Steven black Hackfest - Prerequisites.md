[https://github.com/StevenBlack/hackfest](https://github.com/StevenBlack/hackfest)
   

**Analyzing Bitcoin subject matter**  
==Here we try to picture and resolve why Bitcoin is so hard to explain. We start by picking 21 facets to be explained. We could have picked 40 facets, but 21 is ample for now.==  
==If we list Bitcoin's salient subjects, and cross-reference among them for prerequisite relationships, we get a table that looks like this.==

[![Base concepts and their prereqisite relationships](Exported%20image%2020251228191608-0.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/base-concepts-related.png)

**All matrices can be represented as a graph network**==. Here's the graph network of these prerequisite relationships. What a mess! Let's try to make sense of this.==

[![Base concepts and their prereqisite relationships](Exported%20image%2020251228191609-1.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/base-concepts-graph-1.png)

==Let's see a== **layered graph layout** ==to visualize the subject prerequisite relationships. This is a little better, but it's still a mess.==

[![Layered format for the network graph](Exported%20image%2020251228191609-2.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/base-concepts-layered.png)

==We can== **analyze the network graph for cliques**==. This is interesting because it shows how some concepts are more tightly related. This seems to be is a promising starting point for segmenting the subject matter.==

[![Cliques in the network graph](Exported%20image%2020251228191610-3.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/base-concepts-cliques.png)

==What if we score subjects for their prerequisite value, their complexity (the number of prerequisites), and subtract the complexity score from the prerequisite value?==  
==In other words, the strategy is to start with the subjects that have the highest prerequisite value, and the lowest complexity.==  
==This gives us a pretty nice roadmap! The third column in this table leads with the simpler subjects that partially unlock the greatest number most complex subjects.==

|   |   |   |
|---|---|---|
|**prerequisite value (P)**|**complexity (C)**|**P - C**|
|[![alt text](Exported%20image%2020251228191611-4.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/scores-prerequisites.png)|[![alt text](Exported%20image%2020251228191614-5.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/scores-complexities.png)|[![alt text](Exported%20image%2020251228191626-6.png)](https://github.com/StevenBlack/hackfest/blob/master/assets/scores-prerequisites-complexities.png)|

==So let's run in that order, and see how it goes.==
 \> From \<[https://github.com/StevenBlack/hackfest](https://github.com/StevenBlack/hackfest)\>