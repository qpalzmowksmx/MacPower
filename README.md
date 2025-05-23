# MacPower

sudo python3 old.py
sudo python3 main.py

old.py     터미널용으로 해보는중
main.py    GUI로 해보는중

둘다 미완성입니다.


https://scolpion.tistory.com/158

Mac Power Setting

pmset official Doc

Unknown locale, assuming C
PMSET(1)                    General Commands Manual                   PMSET(1)

NAME
     pmset – manipulate power management settings

SYNOPSIS
     pmset [-a | -b | -c | -u] [setting value] [...]
     pmset -u [haltlevel percent] [haltafter minutes] [haltremain minutes]
     pmset -g [option]
     pmset schedule [cancel | cancelall] type date+time [owner]
     pmset repeat cancel
     pmset repeat type weekdays time
     pmset relative [wake | poweron] seconds
     pmset [touch | sleepnow | displaysleepnow | boot]

DESCRIPTION
     pmset manages power management settings such as idle sleep timing, wake
     on administrative access, automatic restart on power loss, etc.

     Note that processes may dynamically override these power management
     settings by using I/O Kit power assertions.  Whenever processes override
     any system power settings, pmset will list those processes and their
     power assertions in -g and -g assertions. See caffeinate(8).

SETTING
     pmset can modify the values of any of the power management settings
     defined below. You may specify one or more setting & value pairs on the
     command-line invocation of pmset.  The -a, -b, -c, -u flags determine
     whether the settings apply to battery ( -b ), charger (wall power) ( -c
     ), UPS ( -u ) or all ( -a ).

     Use a minutes argument of 0 to set the idle time to never for sleep
     disksleep and displaysleep

     pmset must be run as root in order to modify any settings.

SETTINGS
     displaysleep - display sleep timer; replaces 'dim' argument in 10.4
     (value in minutes, or 0 to disable)
     disksleep - disk spindown timer; replaces 'spindown' argument in 10.4
     (value in minutes, or 0 to disable)
     sleep - system sleep timer (value in minutes, or 0 to disable)
     womp - wake on ethernet magic packet (value = 0/1). Same as "Wake for
     network access" in System Settings.
     ring - wake on modem ring (value = 0/1)
     powernap - enable/disable Power Nap on supported machines (value = 0/1)
     proximitywake - On supported systems, this option controls system wake
     from sleep based on proximity of devices using same iCloud id. (value =
     0/1)
     autorestart - automatic restart on power loss (value = 0/1)
     lidwake - wake the machine when the laptop lid (or clamshell) is opened
     (value = 0/1)
     acwake - wake the machine when power source (AC/battery) is changed
     (value = 0/1)
     lessbright - slightly turn down display brightness when switching to this
     power source (value = 0/1)
     halfdim - display sleep will use an intermediate half-brightness state
     between full brightness and fully off  (value = 0/1)
     sms - use Sudden Motion Sensor to park disk heads on sudden changes in G
     force (value = 0/1)
     hibernatemode - change hibernation mode. Please use caution. (value =
     integer)
     hibernatefile - change hibernation image file location. Image may only be
     located on the root volume. Please use caution. (value = path)
     ttyskeepawake - prevent idle system sleep when any tty (e.g. remote login
     session) is 'active'. A tty is 'inactive' only when its idle time exceeds
     the system sleep timer. (value = 0/1)
     networkoversleep - this setting affects how OS X networking presents
     shared network services during system sleep. This setting is not used by
     all platforms; changing its value is unsupported.
     destroyfvkeyonstandby - Destroy File Vault Key when going to standby
     mode. By default File vault keys are retained even when system goes to
     standby. If the keys are destroyed, user will be prompted to enter the
     password while coming out of standby mode.(value: 1 - Destroy, 0 -
     Retain)

GETTING
     -g (with no argument) will display the settings currently in use.
     -g live displays the settings currently in use.
     -g custom displays custom settings for all power sources.
     -g cap displays which power management features the machine supports.
     -g sched displays scheduled startup/wake and shutdown/sleep events.
     -g ups displays UPS emergency thresholds.
     -g ps / batt displays status of batteries and UPSs.
     -g pslog displays an ongoing log of power source (battery and UPS) state.
     -g rawlog displays an ongoing log of battery state as read directly from
     battery.
     -g therm shows thermal conditions that affect CPU speed. Not available on
     all platforms.
     -g thermlog shows a log of thermal notifications that affect CPU speed.
     Not available on all platforms.
     -g assertions displays a summary of power assertions. Assertions may
     prevent system sleep or display sleep. Available 10.6 and later.
     -g assertionslog shows a log of assertion creations and releases.
     Available 10.6 and later.
     -g sysload displays the "system load advisory" - a summary of system
     activity available from the IOGetSystemLoadAdvisory API. Available 10.6
     and later.
     -g sysloadlog displays an ongoing log of lives changes to the system load
     advisory. Available 10.6 and later.
     -g ac / adapter will display details about an attached AC power adapter.
     Only supported for MacBook and MacBook Pro.
     -g log displays a history of sleeps, wakes, and other power management
     events. This log is for admin & debugging purposes.
     -g uuid displays the currently active sleep/wake UUID; used within OS X
     to correlate sleep/wake activity within one sleep cycle.  history
     -g uuidlog displays the currently active sleep/wake UUID, and prints a
     new UUID as they're set by the system.
     -g history is a debugging tool. Prints a timeline of system sleeplwake
     UUIDs, when enabled with boot-arg io=0x3000000.
     -g historydetailed Prints driver-level timings for a sleep/wake. Pass a
     UUID as an argument.
     -g powerstate [class names] Prints the current power states for I/O Kit
     drivers. Caller may provide one or more I/O Kit class names (separated by
     spaces) as an argument. If no classes are provided, it will print all
     drivers' power states.
     -g powerstatelog [-i interval] [class names] Periodically prints the
     power state residency times for some drivers. Caller may provide one or
     more I/O Kit class names (separated by spaces). If no classes are
     provided, it will log the IOPower plane's root registry entry. Caller may
     specify a polling interval, in seconds with -i <polling interval>;
     otherwise it defaults to 5 seconds.
     -g stats Prints the counts for number sleeps and wakes system has gone
     thru since boot.
     -g systemstate Prints the current power state of the system and available
     capabilites.
     -g everything Prints output from every argument under the GETTING header.
     This is useful for quickly collecting all the output that pmset provides.
     Available in 10.8.

SAFE SLEEP ARGUMENTS
     hibernatemode supports values of 0, 3, or 25. Whether or not a
     hibernation image gets written is also dependent on the values of standby
     and autopoweroff

     For example, on desktops that support standby a hibernation image will be
     written after the specified standbydelay time. To disable hibernation
     images completely, ensure hibernatemode standby and autopoweroff are all
     set to 0.

     hibernatemode = 0 by default on desktops. The system will not back memory
     up to persistent storage. The system must wake from the contents of
     memory; the system will lose context on power loss. This is,
     historically, plain old sleep.

     hibernatemode = 3 by default on portables. The system will store a copy
     of memory to persistent storage (the disk), and will power memory during
     sleep. The system will wake from memory, unless a power loss forces it to
     restore from hibernate image.

     hibernatemode = 25 is only settable via pmset. The system will store a
     copy of memory to persistent storage (the disk), and will remove power to
     memory. The system will restore from disk image. If you want
     "hibernation" - slower sleeps, slower wakes, and better battery life, you
     should use this setting.

     Please note that hibernatefile may only point to a file located on the
     root volume.

STANDBY ARGUMENTS
     standby causes kernel power management to automatically hibernate a
     machine after it has slept for a specified time period. This saves power
     while asleep. This setting defaults to ON for supported hardware. The
     setting standby will be visible in pmset -g if the feature is supported
     on this machine.

     standbydelayhigh and standbydelaylow specify the delay, in seconds,
     before writing the hibernation image to disk and powering off memory for
     Standby.  standbydelayhigh is used when the remaining battery capacity is
     above highstandbythreshold , and standbydelaylow is used when the
     remaining battery capacity is below highstandbythreshold.

     highstandbythreshold has a default value of 50 percent.

     autopoweroff is enabled by default on supported platforms as an
     implementation of Lot 6 to the European Energy-related Products
     Directive. After sleeping for <autopoweroffdelay> seconds, the system
     will write a hibernation image and go into a lower power chipset sleep.
     Wakeups from this state will take longer than wakeups from regular sleep.

     autopoweroffdelay specifies the delay, in seconds, before entering
     autopoweroff mode.

UPS SPECIFIC ARGUMENTS
     UPS-specific arguments are only valid following the -u option. UPS
     settings also have an on/off value. Use a -1 argument instead of percent
     or minutes to turn any of these settings off. If multiple halt conditions
     are specified, the system will halt on the first condition that occurs in
     a low power situation.

     haltlevel - when draining UPS battery, battery level at which to trigger
     an emergency shutdown (value in %)
     haltafter - when draining UPS battery, trigger emergency shutdown after
     this long running on UPS power (value in minutes, or 0 to disable)
     haltremain - when draining UPS battery, trigger emergency shutdown when
     this much time remaining on UPS power is estimated (value in minutes, or
     0 to disable)

     Note: None of these settings are observed on a system with support for an
     internal battery, such as a laptop. UPS emergency shutdown settings are
     for desktop and server only.

SCHEDULED EVENT ARGUMENTS
     pmset allows you to schedule system sleep, shutdown, wakeup and/or power
     on. "schedule" is for setting up one-time power events, and "repeat" is
     for setting up daily/weekly power on and power off events. Note that you
     may only have one pair of repeating events scheduled - a "power on" event
     and a "power off" event. For sleep cycling applications, pmset can
     schedule a "relative" wakeup or poweron to occur in seconds from the end
     of system sleep/shutdown, but this event cannot be cancelled and is
     inherently imprecise.

     type - one of sleep, wake, poweron, shutdown, wakeorpoweron
     date/time - "MM/dd/yy HH:mm:ss" (in 24 hour format; must be in quotes)
     time - HH:mm:ss
     weekdays - a subset of MTWRFSU ("M" and "MTWRF" are valid strings)
     owner - a string describing the person or program who is scheduling this
     one-time power event (optional)

POWER SOURCE ARGUMENTS
     -g with a 'batt' or 'ps' argument will show the state of all attached
     power sources.

     -g with a 'pslog' or 'rawlog' argument is normally used for debugging,
     such as isolating a problem with an aging battery.

OTHER ARGUMENTS
     boot - tell the kernel that system boot is complete (normally LoginWindow
     does this). May be useful to Darwin users.
     touch - PM re-reads existing settings from disk.
     noidle - pmset prevents idle sleep by creating a PM assertion to prevent
     idle sleep(while running; hit ctrl-c to cancel). This argument is
     deprecated in favor of caffeinate(8). Please use caffeinate(8) instead.
     sleepnow - causes an immediate system sleep.
     restoredefaults - Restores power management settings to their default
     values.
     displaysleepnow - causes display to go to sleep immediately.
     resetdisplayambientparams - resets the ambient light parameters for
     certain Apple displays.
     dim - deprecated in 10.4 in favor of 'displaysleep'. 'dim' will continue
     to work.
     spindown - deprecated in 10.4 in favor of 'disksleep'. 'spindown' will
     continue to work.

EXAMPLES
     This command sets displaysleep to a 5 minute timer on battery power,
     leaving other settings on battery power and other power sources
     unperturbed.

     pmset -b displaysleep 5

     Sets displaysleep to 10, disksleep to 10, system sleep to 30, and turns
     on WakeOnMagicPacket for ALL power sources (AC, Battery, and UPS) as
     appropriate

     pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1

     For a system with an attached and supported UPS, this instructs the
     system to perform an emergency shutdown when UPS battery drains to below
     40%.

     pmset -u haltlevel 40

     For a system with an attached and supported UPS, this instructs the
     system to perform an emergency shutdown when UPS battery drains to below
     25%, or when the UPS estimates it has less than 30 minutes remaining
     runtime. The system shuts down as soon as either of these conditions is
     met.

     pmset -u haltlevel 25 haltremain 30

     For a system with an attached and supported UPS, this instructs the
     system to perform an emergency shutdown after 2 minutes of running on UPS
     battery power.

     pmset -u haltafter 2

     Schedules the system to automatically wake from sleep on July 4, 2016, at
     8PM.

     pmset schedule wake "07/04/16 20:00:00"

     Schedules a repeating shutdown to occur each day, Tuesday through
     Saturday, at 11AM.

     pmset repeat shutdown TWRFS 11:00:00

     Schedules a repeating wake or power on event every tuesday at 12:00 noon,
     and a repeating sleep event every night at 8:00 PM.

     pmset repeat wakeorpoweron T 12:00:00 sleep MTWRFSU 20:00:00

     Cancels all scheduled system sleep, shutdown, wake, and power on events.

     pmset repeat cancel

     Prints the power management settings in use by the system.

     pmset -g

     Prints a snapshot of battery/power source state at the moment.

     pmset -g batt

     If your system suddenly sleeps on battery power with 20-50% of capacity
     remaining, leave this command running in a Terminal window. When you see
     the problem and later power and wake the computer, you'll be able to
     detect sudden discontinuities (like a jump from 30% to 0%) indicative of
     an aging battery.

     pmset -g pslog

SEE ALSO
     caffeinate(8)

FILES
     All changes made through pmset are saved in a persistent preferences file
     (per-system, not per-user) at
     /Library/Preferences/SystemConfiguration/com.apple.PowerManagement.plist

     Scheduled power on/off events are stored separately in
     /Library/Preferences/SystemConfiguration/com.apple.AutoWake.plist

     pmset modifies the same file that System Settings modifies.

Darwin                         November 9, 2012                         Darwin

[Process completed]

