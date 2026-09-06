https://www.youtube.com/watch?v=q257UmHSP5E

Another layer on top of local models and remote models.


This tool provides a lot of useful tools for abstracting the models with the tasks needing completion.

Even when only using a simple llama.cpp server I think setup up bifrost as well is probably worth it.

* Drop-in Replacement - This is probably the number one thing I'm interested in. These AI requests should be treated like a raw material. Some models may have advantages over others for some things but I am really using up compute resources and expecting some refined material (easy to read and maintain code) out. 
* Load Balancing - model specific filtering. I'd like to hide which model is being used for what type of task from end users. A general chat model might have some idea about what type of question is being asked and what model is best suited for answering this question.



# Prerequisites
[llama seteup](../llama/LLAMA.md)


# Setup
[bifrost](../../bifrost/README.md)

