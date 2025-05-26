নিচে তোমার দেওয়া কোডটি লাইনে লাইনে ব্যাখ্যা করলাম বাংলা ভাষায় — কেন লিখা হয়েছে, কী করে, আর এইভাবে কেন করা হয়েছে — সব কিছু স্পষ্ট ও বিস্তারিতভাবে ব্যাখ্যা করেছি:

📦 import util
python
Copy
Edit
import util
🔍 ব্যাখ্যা:

util.py ফাইলটি হচ্ছে একটি সহায়ক ফাইল, যেটা Pacman AI প্রজেক্টে দেওয়া থাকে।

এর মধ্যে Stack, Queue, এবং PriorityQueue ক্লাস আছে, যেগুলো তোমার DFS, BFS, UCS, A* ইমপ্লিমেন্ট করতে লাগবে।

🔧 class SearchProblem:
python
Copy
Edit
class SearchProblem:
🔍 ব্যাখ্যা:

এটা একটা অ্যাবস্ট্রাক্ট ক্লাস (interface/blueprint)। তুমি সরাসরি এটা ব্যবহার করো না।

এর child class বা instance পাবে যখন Pacman maze environment চলবে।

এর কাজ হচ্ছে Search Problem কে define করা।

📍 Start State Function
python
Copy
Edit
def getStartState(self):
    util.raiseNotDefined()
🔍 ব্যাখ্যা:

এই ফাংশনটি শুরু পয়েন্ট (Pacman-এর শুরু অবস্থান) রিটার্ন করবে।

util.raiseNotDefined() হচ্ছে placeholder → এখনো ইমপ্লিমেন্ট করা হয়নি বলে error দিবে।

🎯 Goal State Checker
python
Copy
Edit
def isGoalState(self, state):
    util.raiseNotDefined()
🔍 ব্যাখ্যা:

এই ফাংশন চেক করে যে state-টা কি গন্তব্য (goal) কিনা।

যদি হয়, তাহলে True রিটার্ন করবে।

🔀 Successor Function
python
Copy
Edit
def getSuccessors(self, state):
    util.raiseNotDefined()
🔍 ব্যাখ্যা:

এটা state এর সব সম্ভাব্য পরবর্তী স্টেট (সন্তান নোড) রিটার্ন করবে।

ফরম্যাট: [(successor, action, cost), ...]

💰 Cost Calculation Function
python
Copy
Edit
def getCostOfActions(self, actions):
    util.raiseNotDefined()
🔍 ব্যাখ্যা:

কোনো action লিস্ট (যেমন ['South', 'South', 'West']) দিলে, তার মোট cost রিটার্ন করে।

🎮 tinyMazeSearch
python
Copy
Edit
def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]
🔍 ব্যাখ্যা:

এটা ম্যানুয়ালি লেখা একটা সলিউশন tinyMaze-এর জন্য।

মানে Pacman-কে সঠিকভাবে গন্তব্যে নিতে South, West নির্দেশ দেওয়া হয়েছে।

এটা testing purpose-এ দেওয়া হয়।

🔍 Depth-First Search (DFS)
python
Copy
Edit
def depthFirstSearch(problem):
🔍 ব্যাখ্যা:

এটি DFS algorithm ইমপ্লিমেন্ট করে।

এটি একটি uninformed search → কোনো heuristic বা cost ব্যবহার করে না।

🎯 Get Start Node
python
Copy
Edit
startingNode = problem.getStartState()
if problem.isGoalState(startingNode):
    return []
🔍 ব্যাখ্যা:

getStartState() থেকে শুরু স্টেট পাওয়া যাচ্ছে।

যদি শুরুতেই গন্তব্যে থাকে তাহলে খালি লিস্ট ([]) ফেরত দিচ্ছে (মানে কোনো পদক্ষেপ দরকার নেই)।

🧱 Stack & Visited List
python
Copy
Edit
dfsstack = util.Stack()
visitedNodes = []
dfsstack.push((startingNode, []))
🔍 ব্যাখ্যা:

DFS এর জন্য Stack ব্যবহার করা হয় কারণ এটা LIFO (Last In First Out) স্ট্রাকচার।

visitedNodes লিস্টে আমরা যেসব নোড ভিজিট করেছি তা রাখি, যেন লুপে না পড়ি।

Stack-এ প্রথমে (state, actions_list) tuple পুশ করা হয়।

🔄 Main Loop
python
Copy
Edit
while not dfsstack.isEmpty():
    currentNode, actions = dfsstack.pop()
🔍 ব্যাখ্যা:

যতক্ষণ Stack ফাঁকা না হয়, ততক্ষণ লুপ চালবে।

Stack থেকে এক এক করে state বের করে এনে চেক করা হবে।

✅ Visit Node & Goal Check
python
Copy
Edit
if currentNode not in visitedNodes:
    visitedNodes.append(currentNode)
    if problem.isGoalState(currentNode):
        return actions
🔍 ব্যাখ্যা:

যদি বর্তমান স্টেট আগের মতো না হয়, তাহলে visited লিস্টে রাখি।

যদি গন্তব্যে পৌঁছে যাই, তাহলে এখন পর্যন্ত করা actions রিটার্ন করি।

🧭 Expand Child Nodes
python
Copy
Edit
for nextNode, action, cost in problem.getSuccessors(currentNode):
    nwAction = actions + [action]
    dfsstack.push((nextNode, nwAction))
🔍 ব্যাখ্যা:

বর্তমান স্টেট থেকে পাওয়া successor গুলোর জন্য নতুন অ্যাকশন লিস্ট বানাই।

Stack-এ push করি যাতে পরের বার সে নোড ঘুরে দেখা হয়।

🌐 Breadth-First Search (BFS)
python
Copy
Edit
def breadthFirstSearch(problem):
🔍 ব্যাখ্যা:

এটা BFS algorithm → Queue ব্যবহার করে।

DFS-এর মতোই, কিন্তু Stack-এর জায়গায় Queue।

🔄 BFS Logic (Same as DFS, but FIFO)
python
Copy
Edit
bfsQueue = util.Queue()
visitedNodes = []
bfsQueue.push((startingNode, []))
🔍 ব্যাখ্যা:

Queue ব্যবহার করায় প্রথমে আসা স্টেট আগে প্রসেস হয়।

FIFO (First In First Out) structure → level wise traversal হয়।

