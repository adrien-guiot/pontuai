# Pontu AI  
    A simple IA capable of playing a single turn of pontu.
    
### usage
the AI is accessible via a Post to https://pontuai-qy3fcdg7ya-ew.a.run.app/ai

At the time of writing this, the URL is not usable with the provided app hosted on Heroku due to CORS issues.
  
# Limitations
   three points seems importants to me concerning this project
   1. 0 tests. I am not expecting to maintain this project, so I'm losing the single most important reason to test a project.
   If you expected testing as part of the exercise, please let me know and I'll do my Best to provide as soon as possible.
   2. simplicity of the AI. That AI is quite simple and determinist
   3. prone to Error and no errors management. I have decided to go with some "general rules", a bridge should always be "left to right" or "top to bottom".
   any other will mostly be counted as a bridge not existing. and if no solution is possible (including inversed bridges), an error will occured on the AI side.
   
   
   once again, I choose to make those choices so I could make it the few hours I spent on the project, And I would gladly take some time to talk about those choices or about what I would do without those kind of limitation.
   
   
# About _Not the AI_

   I decided to try something I never used before, which is the serverless service of GCP "Cloud run".
   
   It cost me a few more hours to set up the dockerfile, the gcp project, and really understanding what I was doing.
   
   
# What's next

   If I had to spend more time on the project, I would start by fixing limits 1 and 3 in order to make it more resilient. Then I would rewrite part of the code, like in the `Board` class where I recreate a new board for every possible move/bridge removal in order to find the best actions. It quite costly in terms of time/computation.

# Thank you

   I'm always having a blast doing those kind of tests/projects, even challenging myself to try things I never have before, like Cloud run here
   And it's always interesting to have feedback from a peer.

