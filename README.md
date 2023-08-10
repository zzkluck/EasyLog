# EasyLog

**EasyLog尝试实现高敏捷性的日志解析/日志模板提取**。早些年常见的日志解析算法会尝试使用一个预处理步骤——使用正则表达式匹配并替换一部分日志中的词，来降低日志解析的难度。[Drain](https://github.com/logpai/Drain3)中提到：“*we only consider tokens that do not contain digits in this step*”，这个策略听着不太靠谱，但它比它听起来的更有效。对于大量的其实没那么复杂的日志来说，这样就够了。要注意，如果你想追求当下比较热门的“常变量区分完全正确”的日志解析，使用这种简单方法需要你付出额外的努力。

EasyLog突出的就是一个快，简单测试下，python实现下的单线程处理能力在每秒20000-40000条日志左右，继续改为更高效的语言实现或添加多线程支持（话说python这两天是不是要取消GIL了）都能大幅提高效率。深度学习模型加载个数据集的功夫，EasyLog可能已经根据初步结果迭代两轮了。当然，代价是它没深度学习模型那么**智能**，你得多操心点事情。

该库包含了EasyLog的源代码，说实话也没啥东西，主要是变着花地使用正则表达式。以及一个简单的benchmark例子，希望能帮助您尽快了解该代码如何使用。

**EasyLog tries to achieve high agility in log parsing/log template extraction**. Common log parsing algorithms in earlier years would try to reduce the difficulty of log parsing by using a preprocessing step - matching and replacing a portion of the words in the log using regular expressions. The strategy mentioned in [Drain](https://github.com/logpai/Drain3), "*we only consider tokens that do not contain digits in this step*," doesn't sound very plausible, but it's more effective than it sounds. For a large number of logs that aren't really that complex, this will suffice. Note that if you're going for the hot "constant variable differentiation is exactly right" log parsing, this simple approach will require extra effort on your part.

EasyLog highlights a fast, simple test, python implementation of the single-threaded processing capacity of 20,000-40,000 logs per second or so, continue to change to a more efficient language implementation or add multi-threaded support (that is, python two days is not to cancel the GIL) can greatly improve efficiency. In the time it takes a deep learning model to load a dataset, EasyLog may have already done two rounds of iterations based on the initial results. Of course, the tradeoff is that it's not as **smart** as the deep learning model, so you'll have to worry about things a bit more.

The library contains the source code for EasyLog, which to be honest doesn't have much to offer, mainly regular expressions in a fancy way. As well as a simple benchmark example, which will hopefully help you get up to speed on how the code works.

## Prerequisites:
* 只有Python3! EasyLog被设计不依赖额外的库运行。
* Only Python3! EasyLog is designed to run without relying on additional libraries.

## Installing:
1. Download the project code files with:

   `git clone https://github.com/zzkluck/EasyLog.git`

2. Go to the project directory

   `cd EasyLog`

## Usage:

To use the model, open a terminal, change directory to this project code, run the command: 

`python run.py`


## Project Structure:
1. run.py: benchmarck入口地址，提供了代码的使用用例；
2. easylog.py: EasyLog方法的实现；
3. settings.py: 对于16个日志数据集给定的预处理规则；
4. evaluator.py: [logparser](https://github.com/logpai/logparser)中[evaluator.py](https://github.com/logpai/logparser/blob/master/logparser/utils/evaluator.py)的重新实现，不再依赖外部库。


## Data Format:
* 我们使用LogHub提供的数据，可以在[LogHub](https://github.com/logpai/loghub)找到。