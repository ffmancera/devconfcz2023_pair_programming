## Problem

We have asked bigbrainGPT to create a script to parse a log file we have collected from a customer case.

The log file will contain lines like this:

```
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.3702] device (wlp0s20f3): supplicant interface state: disconnected -> inactive
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.3702] device (p2p-dev-wlp0s20f3): supplicant management interface state: disconnected -> inactive
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.3755] device (wlp0s20f3): supplicant interface state: inactive -> authenticating
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.3755] device (p2p-dev-wlp0s20f3): supplicant management interface state: inactive -> authenticating
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.4194] device (wlp0s20f3): supplicant interface state: authenticating -> associating
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.4195] device (p2p-dev-wlp0s20f3): supplicant management interface state: authenticating -> associating
Jun 17 09:31:34 fedora NetworkManager[1398]: <info>  [1686987094.4402] device (wlp0s20f3): supplicant interface state: associating -> completed
```

We want to do 2 different things:

1. Calculate for how long is the interface in "completed" state
2. Log the timestamps of "authenticating" events


Our AI did it wrong and the script is not working properly.. could you fix it?

## Correct output:

```
Device was on for 1879.0 seconds
Timestamps of auth events:
	Jun 17 09:31:34
	Jun 17 10:02:53
```
