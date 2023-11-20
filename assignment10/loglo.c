#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

typedef struct {
    double x;
    double y;
} Position;

void executeCommand(const char* command, Position* position, double* angle) {
    char action[3];
    double value;
    sscanf(command, "%s %lf", action, &value);

    if (strcmp(action, "fd") == 0) {
        position->x += value * cos(*angle * M_PI / 180);
        position->y += value * sin(*angle * M_PI / 180);
    } else if (strcmp(action, "bk") == 0) {
        position->x -= value * cos(*angle * M_PI / 180);
        position->y -= value * sin(*angle * M_PI / 180);
    } else if (strcmp(action, "lt") == 0) {
        *angle += value;
    } else if (strcmp(action, "rt") == 0) {
        *angle -= value;
    }
}

int main() {
    int testCases;
    scanf("%d", &testCases);

    for (int i = 0; i < testCases; i++) {
        int numCommands;
        scanf("%d", &numCommands);
        char command[20];
        
        Position position = {0.0, 0.0};
        double angle = 0.0;

        for (int j = 0; j < numCommands; j++) {
            scanf(" %[^\n]", command);
            executeCommand(command, &position, &angle);
        }

        printf("%d\n", (int)round(sqrt(position.x * position.x + position.y * position.y)));
    }

    return 0;
}
