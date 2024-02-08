.. _usage:

Usage
=====

The simplest way to get started is to run the executable ``voiager`` from a terminal within the `Voiager/ <https://github.com/nhamaus/Voiager/tree/main>`_ package directory. This launches *Voiager* following `launch.py <https://github.com/nhamaus/Voiager/blob/main/voiager/launch.py>`_ with python (version 3). For further help on its usage, type:

.. code-block:: bash

   voiager --help

*Voiager* is set up to perform an example run from the `Beyond-2pt <https://github.com/ANSalcedo/Beyond2ptMock>`_ blind data challenge, based on a simulated light-cone in a \ *w*\ CDM cosmology (`C_mock_lightcone.h5 <https://github.com/ANSalcedo/Beyond2ptMock/blob/main/C_mock_lightcone.h5>`_). The input data is retrieved from the `catalogs/ <https://github.com/nhamaus/Voiager/tree/main/catalogs/>`_ folder including void catalogs produced with `VIDE <https://bitbucket.org/cosmicvoids/vide_public/wiki/Home/>`_, while the output of the code is stored in the `results/ <https://github.com/nhamaus/Voiager/tree/main/results/>`_ directory.

.. note::
    The example data in `catalogs/ <https://github.com/nhamaus/Voiager/tree/main/catalogs/>`_ and the example results in `results/ <https://github.com/nhamaus/Voiager/tree/main/results/>`_ are not automatically downloaded upon installation, but they can be accessed via the repository. The `catalogs/ <https://github.com/nhamaus/Voiager/tree/main/catalogs/>`_ folder can be downloaded as a compressed archive `catalogs.tar.gz <https://github.com/nhamaus/Voiager/releases/download/v0.1.0/catalogs.tar.gz>`_ and unpacked via

    .. code-block:: bash

       tar -xvzf catalogs.tar.gz

The executable ``voiager`` will produce the following output:

.. literalinclude:: ../log.txt
    :language: python

.. note::
    All the parameters of *Voiager* are configured in the file `params.yaml <https://github.com/nhamaus/Voiager/blob/main/voiager/params.yaml>`_, which is used as default configuration. You can also point to your customized parameter file in `yaml <https://pyyaml.org/>`_ format like this:
    
    .. code-block:: bash
   
        voiager 'path/to/parameter_file.yaml'
    
    Previously calculated data vectors are saved in the file `stacks.dat <https://github.com/nhamaus/Voiager/blob/main/results/Beyond2pt/C_mock_lightcone_0240/stacks.dat>`_, this step in the pipeline will be skipped in case the file already exists (i.e., it needs to be removed to start a new calculation, but note that it requires about 32GB of available memory). Similarly, the files named `chains.dat <https://github.com/nhamaus/Voiager/blob/main/results/Beyond2pt/C_mock_lightcone_0240/chains.dat>`_ contain previously run MCMCs, which the code will continue sampling when found. Human readable ASCII versions of the chains are also produced.

The file `params.yaml <https://github.com/nhamaus/Voiager/blob/main/voiager/params.yaml>`_ contains the main adjustable parameters of the code, each of which appears with a brief comment about its meaning:

.. literalinclude:: ../voiager/params.yaml
    :language: yaml