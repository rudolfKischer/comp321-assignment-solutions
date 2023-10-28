#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

bool is_valid_combination(int team[5]) {
    int G = team[0];
    int W = team[1];
    int D = team[2];
    int L = team[3];
    int P = team[4];

    if (G != W + D + L) return false;
    if (P != 3*W + D) return false;
    return true;
}

void fill_missing_values(int team[5], int result[5]) {
    int possible_values[401];
    for (int i = 0; i < 401; i++) {
        possible_values[i] = i;
    }

    int missing_indices[5];
    int missing_count = 0;
    for (int i = 0; i < 5; i++) {
        if (team[i] == -1) {  // Using -1 instead of "?"
            missing_indices[missing_count] = i;
            missing_count++;
        }
    }

    for (int i = 0; i < 401; i++) {
        for (int j = 0; j < 401; j++) {
            int temp[5];
            for (int k = 0; k < 5; k++) {
                temp[k] = team[k];
            }
            temp[missing_indices[0]] = possible_values[i];
            temp[missing_indices[1]] = possible_values[j];

            if (is_valid_combination(temp)) {
                for (int k = 0; k < 5; k++) {
                    result[k] = temp[k];
                }
                return;
            }
        }
    }
}

int main() {
    int N;
    // Uncomment this section to read input
    scanf("%d", &N);
    int teams[N][5];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 5; j++) {
            char input[20];
            scanf("%s", input);
            if (input[0] == '?') {
                teams[i][j] = -1;
            } else {
                sscanf(input, "%d", &teams[i][j]);
            }
        }
    }

    // Comment out this section when reading actual input
    // N = 1000;
    // int teams[N][5];
    // srand(time(NULL));

    // for (int i = 0; i < N; i++) {
    //     int W = rand() % 101;
    //     int D = rand() % (101 - W);
    //     int L = 100 - W - D;
    //     int P = 3*W + D;
    //     int team[5] = {100, W, D, L, P};

    //     for (int j = 0; j < (rand() % 3); j++) {
    //         team[rand() % 5] = -1;  // Using -1 instead of "?"
    //     }
    //     for (int j = 0; j < 5; j++) {
    //         teams[i][j] = team[j];
    //     }
    // }

    clock_t start, end;
    double cpu_time_used;
    start = clock();

    for (int i = 0; i < N; i++) {
        int result[5];
        fill_missing_values(teams[i], result);
        for (int j = 0; j < 5; j++) {
            printf("%d ", result[j]);
        }
        printf("\n");
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    // printf("%f\n", cpu_time_used);

    return 0;
}
