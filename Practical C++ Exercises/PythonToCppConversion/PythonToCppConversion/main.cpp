/*
p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print p
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<double> movex(vector<double> probability, int step, double pExact, double pOvershoot, double pUndershoot) {
    
    if (step == 0) {
        return probability;
    }

    vector<double> result;
    for (int i = 0; i < probability.size(); i++)
    {
        double s = pExact * probability[(i - step) % probability.size()];
        s = s + (pOvershoot * probability[(i - step-1) % probability.size()]);
        s = s + (pUndershoot * probability[(i - step+1) % probability.size()]);

        result.push_back(s);

    }
    return result;



}



vector<double> sense(vector<double> probability, vector<string> world, string s, double pHit, double pMiss)
{
    vector<double> result;
    double total = 0;
    for (int i = 0; i < probability.size(); i++) {
        if (world[i] == s) {
            total += probability[i] * pHit;
            result.push_back(probability[i] * pHit);
        }
        else {
            total += probability[i] * pMiss;
            result.push_back(probability[i] * pMiss);
        }
    }

    for (int i = 0; i < probability.size(); i++)
    {
        result[i] = result[i] / total;
    }
    return result;

} 


int main() {

    vector<double> probability(5, 0.2);
    vector<string> world(5);
    world[0] = "green";
    world[3] = "green";
    world[4] = "green";
    world[1] = "red";
    world[2] = "red";

    string s = "red";
    double pHit = 0.6;
    double pMiss = 0.2;

    double pExact = 0.8;
    double pOvershoot = 0.1;
    double pUndershoot = 0.1;
    vector<string> measurements = { "red", "green" };
    vector<double> motions = { 1, 1 };

    vector<double> result = sense(probability, world, s, pHit, pMiss);

    cout << "--------------Probability--------------------" << endl;
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }
    cout << "-------------- Probability **** END --------------------" << endl;

    

     for (int i = 0; i < measurements.size(); i++) {

         probability = sense(probability, world, measurements[i], pHit, pMiss);
         probability = movex(probability, motions[i], pExact, pOvershoot, pUndershoot);
     }

     for (int i = 0; i < probability.size(); i++) {
         cout << probability[i] << " ";
     }
     cout << endl;
    
}




