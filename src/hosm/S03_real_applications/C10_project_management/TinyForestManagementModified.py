import mdptoolbox.example

from hosm.S03_real_applications.C10_project_management.TinyForestManagement import forest


def tfmm():
    P, R = forest(
        S=3,
        r1=4,
        r2=2,
        p=0.8
    )

    print(P[0])
    print(P[1])

    print(R[:, 0])
    print(R[:, 1])

    gamma = 0.9

    PolIterModel = mdptoolbox.mdp.PolicyIteration(P, R, gamma)

    PolIterModel.run()

    print(PolIterModel.V)

    print(PolIterModel.policy)

    print(PolIterModel.iter)

    print(PolIterModel.time)


if __name__ == "__main__":
    tfmm()
