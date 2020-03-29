#!/bin/bash
set -uo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR
IFS=$'\n\t'

chip0=/sys/class/pwm/pwmchip0
pwm0=$chip0/pwm0
pwm1=$chip0/pwm1

echo 0 > $chip0/export
echo 1 > $chip0/export
echo 20000000  > $pwm0/period
echo 20000000  > $pwm1/period
echo 1500000 > $pwm0/duty_cycle
echo 1500000 > $pwm1/duty_cycle
echo 1 > $pwm0/enable
echo 1 > $pwm1/enable
