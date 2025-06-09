#include <GL/glut.h>
#include <math.h>

#define PI 3.14159265358979323846
#define N_THETA 100
#define N_W 20

float angleX = 20.0f, angleY = 30.0f;
int lastX, lastY;
int isDragging = 0;

void mobius_strip()
{
    for (int i = 0; i < N_W - 1; ++i)
    {
        float w0 = -0.5f + i * (1.0f / (N_W - 1));
        float w1 = -0.5f + (i + 1) * (1.0f / (N_W - 1));
        glBegin(GL_QUAD_STRIP);
        for (int j = 0; j < N_THETA; ++j)
        {
            float theta = j * (2 * PI / (N_THETA - 1));
            float x0 = (1 + w0 * cos(theta / 2)) * cos(theta);
            float y0 = (1 + w0 * cos(theta / 2)) * sin(theta);
            float z0 = w0 * sin(theta / 2);

            float x1 = (1 + w1 * cos(theta / 2)) * cos(theta);
            float y1 = (1 + w1 * cos(theta / 2)) * sin(theta);
            float z1 = w1 * sin(theta / 2);

            glColor3f(0.5f + 0.5f * cos(theta), 0.5f + 0.5f * sin(theta), 0.7f);
            glVertex3f(x0, y0, z0);
            glVertex3f(x1, y1, z1);
        }
        glEnd();
    }
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    glTranslatef(0, 0, -3.0f);
    glRotatef(angleX, 1, 0, 0);
    glRotatef(angleY, 0, 1, 0);
    mobius_strip();
    glutSwapBuffers();
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, (double)w / h, 1.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
}

void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON)
    {
        if (state == GLUT_DOWN)
        {
            isDragging = 1;
            lastX = x;
            lastY = y;
        }
        else
        {
            isDragging = 0;
        }
    }
}

void motion(int x, int y)
{
    if (isDragging)
    {
        angleY += (x - lastX);
        angleX += (y - lastY);
        lastX = x;
        lastY = y;
        glutPostRedisplay();
    }
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Mobius Strip (OpenGL)");
    glEnable(GL_DEPTH_TEST);
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMouseFunc(mouse);
    glutMotionFunc(motion);
    glutMainLoop();
    return 0;
}