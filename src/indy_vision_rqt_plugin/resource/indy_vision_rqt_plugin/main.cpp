#include "indy_widget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    indy_widget w;
    w.show();
    return a.exec();
}
