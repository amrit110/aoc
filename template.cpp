#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;
using chrono::duration_cast;
using chrono::microseconds;
using chrono::steady_clock;

vector<string> read_input() {
  ifstream f;
  f.open("input.txt");

  vector<string> input;
  string line;

  while (getline(f, line)) {
    input.push_back(line);
  }

  return input;
}

void solve_part1(const vector<string>& input) {}

void solve_part2(const vector<string>& input) {}

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
