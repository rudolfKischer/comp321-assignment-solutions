#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>
#include <algorithm>

bool is_valid_combination(const std::vector<int>& team) {
    int G = team[0];
    int W = team[1];
    int D = team[2];
    int L = team[3];
    int P = team[4];
    
    if (G != W + D + L) return false;
    if (P != 3 * W + D) return false;
    return true;
}

std::vector<int> fill_missing_values(const std::vector<int>& team) {
    std::vector<int> possible_values(101);
    for (int i = 0; i < 101; ++i) possible_values[i] = i;
    std::vector<int> new_team = team;
    std::vector<int> missing_indices;
    
    for (int i = 0; i < 5; ++i) {
        if (team[i] == -1) {
            missing_indices.push_back(i);
        }
    }
    
    if (std::find(missing_indices.begin(), missing_indices.end(), 4) != missing_indices.end()) {
        possible_values.resize(401);
        for (int i = 101; i < 401; ++i) possible_values[i] = i;
    }
    
    int total = 1;
    for (int i = 0; i < missing_indices.size(); ++i) {
        total *= possible_values.size();
    }
    
    for (int i = 0; i < total; ++i) {
        int temp = i;
        for (int j = 0; j < missing_indices.size(); ++j) {
            new_team[missing_indices[j]] = possible_values[temp % possible_values.size()];
            temp /= possible_values.size();
        }
        
        if (is_valid_combination(new_team)) return new_team;
    }
    
    return team;
}

void generate_test_case() {
    srand(static_cast<unsigned int>(time(nullptr)));
    int N = 1000;
    std::vector<std::vector<int>> teams(N, std::vector<int>(5));
    
    for (int i = 0; i < N; ++i) {
        int W = rand() % 101;
        int D = rand() % (101 - W);
        int L = 100 - W - D;
        int P = 3 * W + D;
        
        teams[i] = {100, W, D, L, P};
        for (int j = 0; j < rand() % 3; ++j) {
            teams[i][rand() % 5] = -1;
        }
    }
    
    std::cout << N << std::endl;
    for (const auto& team : teams) {
        for (int i = 0; i < 5; ++i) {
            if (team[i] == -1) std::cout << "? ";
            else std::cout << team[i] << " ";
        }
        std::cout << std::endl;
    }

    clock_t start = clock();
    for (const auto& team : teams) {
        auto filled_values = fill_missing_values(team);
        for (int i = 0; i < 5; ++i) {
            if (filled_values[i] == -1) std::cout << "? ";
            else std::cout << filled_values[i] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << (static_cast<double>(clock() - start) / CLOCKS_PER_SEC) << std::endl;
}

int main() {
    int N;
    std::cin >> N;
    std::vector<std::vector<int>> teams(N, std::vector<int>(5));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 5; ++j) {
            std::string s;
            std::cin >> s;
            if (s == "?") teams[i][j] = -1;
            else teams[i][j] = std::stoi(s);
        }
    }

    for (const auto& team : teams) {
        auto filled_values = fill_missing_values(team);
        for (int i = 0; i < 5; ++i) {
            if (filled_values[i] == -1) std::cout << "? ";
            else std::cout << filled_values[i] << " ";
        }
        std::cout << std::endl;
    }

    // Uncomment to generate test cases
    generate_test_case();

    return 0;
}
