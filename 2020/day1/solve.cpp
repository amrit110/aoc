#include <chrono>
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;
using chrono::duration_cast;
using chrono::microseconds;
using chrono::steady_clock;

vector<int> read_input() {
  ifstream f;
  f.open("input.txt");

  vector<int> input;
  string str;

  while (getline(f, str)) {
    input.push_back(stoi(str));
  }

  return input;
}

void solve_part1(vector<int>& input) {
  unordered_set<int> diff_set;
  for (auto num : input) {
    int diff = 2020 - num;
    if (diff_set.find(diff) == diff_set.end()) {
      diff_set.insert(2020 - diff);
    } else {
      cout << diff * num << endl;
    }
  }
}

void solve_part2(vector<int>& input) {
  const int sum = 2020;
  for (int i = 0; i < input.size(); ++i) {
    unordered_set<int> diff_set;
    int curr_sum = sum - input[i];
    for (int j = i + 1; j < input.size(); ++j) {
      int tmp = curr_sum - input[j];
      if (diff_set.find(tmp) != diff_set.end()) {
        cout << input[i] * input[j] * tmp << endl;
        return;
      } else {
        diff_set.insert(input[j]);
      }
    }
  }
}

int main() {
  auto input = read_input();
  auto st1 = steady_clock::now();
  solve_part1(input);
  cout << "(time taken part1: "
       << duration_cast<microseconds>(steady_clock::now() - st1).count()
       << "[us])\n";
  auto st2 = steady_clock::now();
  solve_part2(input);
  cout << "(time taken part2: "
       << duration_cast<microseconds>(steady_clock::now() - st2).count()
       << "[us])\n";

  return 0;
}
