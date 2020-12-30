from pytracking.evaluation import Tracker, get_dataset, trackerlist


def atom_nfs_uav():
    # Run three runs of ATOM on NFS and UAV datasets
    trackers = trackerlist('atom', 'default', range(3))

    dataset = get_dataset('nfs', 'uav')
    return trackers, dataset

def uav_test():
    # Run DiMP18, ATOM and ECO on the UAV dataset
    trackers = trackerlist('dimp', 'dimp18', range(1)) + \
               trackerlist('atom', 'default', range(1)) + \
               trackerlist('eco', 'default', range(1))

    dataset = get_dataset('uav')
    return trackers, dataset

def dimp_lasot():
    # Run three runs of ATOM on NFS and UAV datasets
    trackers = trackerlist('dimp', 'dimp18', range(2))
    dataset = get_dataset('lasot')

    return trackers, dataset

def eco_lasot():
    # Run three runs of ATOM on NFS and UAV datasets
    trackers = trackerlist('eco', 'default', range(1))
    dataset = get_dataset('lasot')

    return trackers, dataset
