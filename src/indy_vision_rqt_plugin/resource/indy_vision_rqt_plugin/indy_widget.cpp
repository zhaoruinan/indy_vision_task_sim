#include "indy_widget.h"
#include "ui_indy_widget.h"

indy_widget::indy_widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::indy_widget)
{
    ui->setupUi(this);
}

indy_widget::~indy_widget()
{
    delete ui;
}

