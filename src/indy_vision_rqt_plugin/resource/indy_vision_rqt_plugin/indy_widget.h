#ifndef INDY_WIDGET_H
#define INDY_WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class indy_widget; }
QT_END_NAMESPACE

class indy_widget : public QWidget
{
    Q_OBJECT

public:
    indy_widget(QWidget *parent = nullptr);
    ~indy_widget();

private:
    Ui::indy_widget *ui;
};
#endif // INDY_WIDGET_H
