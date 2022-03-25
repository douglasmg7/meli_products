#! /usr/bin/env bash
ERR=0

# # Should run as a root.
# if [ "$EUID" -ne 0 ]; then 
  # echo "Please run as root"
  # exit
# fi


# Check envs.
[[ -z "$ZUNKA_UTIL_SCRIPTS" ]] && printf "error: ZUNKA_UTIL_SCRIPTS enviorment not defined.\n" >&2 && exit 1 
source $ZUNKA_UTIL_SCRIPTS/check_envs.sh \
    ZUNKAPATH \
    MONGODB_HOST \
    MERCADO_LIVRE_USER_ID \
    ZUNKASITE_HOST_PROD \
    ZUNKASITE_USER_PROD \
    ZUNKASITE_PASS_PROD \
    ZUNKASITE_HOST_DEV \
    ZUNKASITE_USER_DEV \
    ZUNKASITE_PASS_DEV \
    MERCADO_LIVRE_PATH \
    MERCADO_LIVRE_START_PRODUCTION_SCRIPT \


# Meli start script.
[[ ! -f $MERCADO_LIVRE_START_PRODUCTION_SCRIPT ]] && printf "error: script $MERCADO_LIVRE_START_PRODUCTION_SCRIPT not exist.\n" >&2 && ERR=1

# Uninstall script not exist.
[[ ! -f $MERCADO_LIVRE_PATH/bin/uninstall-meli-service.sh ]] && printf "error: script $MERCADO_LIVRE_PATH/bin/uninstall-meli-service.sh not exist.\n" >&2 && ERR=1

[[ $ERR != 0 ]] && exit 1

echo "no error"
exit

# Remove meli timer and service.
$MERCADO_LIVRE_PATH/bin/uninstall-meli-service.sh

# Create log dir.
mkdir -p $ZUNKAPATH/log/meli_products

# Make allnations script wide system accessible.
echo Creating symobolic link for meli_products start production script...
sudo ln -s $MERCADO_LIVRE_START_PRODUCTION_SCRIPT /usr/local/bin/meli

# Create aldo timer.
echo "creating '/lib/systemd/system/meli.timer'..."
sudo bash -c 'cat << EOF > /lib/systemd/system/meli.timer
[Unit]
Description=meli timer

[Timer]
OnCalendar=*-*-* 00:00:01
OnCalendar=*-*-* 01:00:00
OnCalendar=*-*-* 02:00:00
OnCalendar=*-*-* 03:00:00
OnCalendar=*-*-* 04:00:00
OnCalendar=*-*-* 05:00:00
OnCalendar=*-*-* 06:00:00
OnCalendar=*-*-* 07:00:00
OnCalendar=*-*-* 08:00:00
OnCalendar=*-*-* 09:00:00
OnCalendar=*-*-* 10:00:00
OnCalendar=*-*-* 11:00:00
OnCalendar=*-*-* 12:00:00
OnCalendar=*-*-* 13:00:00
OnCalendar=*-*-* 14:00:00
OnCalendar=*-*-* 15:00:00
OnCalendar=*-*-* 16:00:00
OnCalendar=*-*-* 17:00:00
OnCalendar=*-*-* 18:00:00
OnCalendar=*-*-* 19:00:00
OnCalendar=*-*-* 20:00:00
OnCalendar=*-*-* 21:00:00
OnCalendar=*-*-* 22:00:00
OnCalendar=*-*-* 23:00:00

Persistent=true

[Install]
WantedBy=timers.target
EOF'

# Create aldo service.
echo "creating '/lib/systemd/system/meli.service'..."
sudo \
    GS=$GS \
    ZUNKAPATH=$ZUNKAPATH \
    ALLNATIONS_DB=$ALLNATIONS_DB \
    ALLNATIONS_USER=$ALLNATIONS_USER \
    ALLNATIONS_PASS=$ALLNATIONS_PASS \
    ZUNKASITE_HOST_DEV=$ZUNKASITE_HOST_DEV \
    ZUNKASITE_USER_DEV=$ZUNKASITE_USER_DEV \
    ZUNKASITE_PASS_DEV=$ZUNKASITE_PASS_DEV \
    ZUNKASITE_HOST_PROD=$ZUNKASITE_HOST_PROD \
    ZUNKASITE_USER_PROD=$ZUNKASITE_USER_PROD \
    ZUNKASITE_PASS_PROD=$ZUNKASITE_PASS_PROD \
    bash -c 'cat << EOF > /lib/systemd/system/meli.service
[Unit]
Description=meli service

[Service]
Type=oneshot
User=douglasmg7
Environment="GS=$GS"
Environment="ZUNKAPATH=$ZUNKAPATH"
Environment="ALLNATIONS_DB=$ALLNATIONS_DB"
Environment="ALLNATIONS_USER=$ALLNATIONS_USER"
Environment="ALLNATIONS_PASS=$ALLNATIONS_PASS"
Environment="RUN_MODE=production"
Environment="ZUNKASITE_HOST_DEV=$ZUNKASITE_HOST_DEV"
Environment="ZUNKASITE_USER_DEV=$ZUNKASITE_USER_DEV"
Environment="ZUNKASITE_PASS_DEV=$ZUNKASITE_PASS_DEV"
Environment="ZUNKASITE_HOST_PROD=$ZUNKASITE_HOST_PROD"
Environment="ZUNKASITE_USER_PROD=$ZUNKASITE_USER_PROD"
Environment="ZUNKASITE_PASS_PROD=$ZUNKASITE_PASS_PROD"
ExecStart=$GS/allnations/bin/fetch-xml-products-and-process.sh
EOF'

sudo systemctl start meli.timer
sudo systemctl enable meli.timer
