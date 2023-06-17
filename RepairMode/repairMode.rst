Repair Mode
===============

.. image:: UpscaledRepairBar.png
   :align: center

----

- The Repair mode aims at creating a 3D printable mesh/removing deformities present in a mesh (watertight, non-self intersecting and manifold mesh).
- In this mode,  users can inspect meshes and fix them, manually or automatically. Users can reduce triangles, smoothen the mesh, perform outer hull extraction, fill holes, etc. 

----

- When a mesh is loaded in MIRA3D software, it is inspected and represented as:

  .. image:: Part_List_Upscaled.png
     :align: center
     :width: 350

  - ❓   Mesh status not updated
  - ⛔  Mesh contains open shells and holes.
  - ⚠️  Mesh contains multiple watertight shells. 
  - ✅  Mesh contains single watertight shell.

----

Auto Repair
+++++++++++

.. image:: autorepair.png
   :align: center
   :width: 350

|

**AutoFix** button repairs the 3D mesh using MIRA3D\'s PROPRIETARY REPAIR ALGORITHM.

User needs to select the file and press the AutoFix button. For example, if the slider is adjusted to 0.8 there will be 20% reduction in the number of triangles.

.. note:: 
  For coarse meshes, it is recommended to avoid triangle reduction by adjusting the slider to unit value.

----

| 

Manual Repair
++++++++++++++++

.. image:: manualRepair.png
    :align: center

Users can enter the manual repair mode by double clicking on the file name (in the part list) or clicking on the **\“Shell repair\”** button. 

Here, users can view individual manifold shells of a mesh. Users can select (by using left click), isolate (by SHIFT + mouse drag) and delete individual shells of a mesh.

Watertight shells are marked in green✅ and open shells (containing holes) are marked in red⛔. Watertight and open shells can be sorted in the shell repair tab by double clicking on **\“Closed\”**.

After editing the shells, users need to click on **\“Update\”** to update the diagnostics.

.. image:: noholesAIUpscaled.png
   :align: center
   :width: 450

|

The tab above represents a repaired mesh, containing a single shell and no holes.

Previous or next 3D mesh can be brought to the tab by clicking on the **“Previous/Next''** button.

Manual Shell Repair
********************

**Steps**

#. In the shell repair tab, double click on the “Closed” (shell) header to view the list of all open and closed shells.
#. Click all closed shells(marked with✅) for any negative volumes. In case of such shells select them and click on the “Fix Inversion” button.
#. Check all open shells (marked with ⛔).

   Cases:

   #. If the holes seem too small to be visually identified or planar, fix them by selecting them and clicking on the **“Fill holes”**  button. Additionally, check for small sized floating shells and eliminate them by clicking on the **“Remove all noise”** button.
   #. If the holes are large and non-planar then look for other open shells which can cover the hole. Unify those shells by selecting them, using the **“Unify selected”** button. Later on remove any extra noise that may be generated and fill the holes using the **“Fill holes”** button.

#. Once all the shells are green, click on the **“Autofix”** button. 

.. note:: 
   The user may also click on **“Unify selected”** instead of **“Autofix”**. However, this is comparatively slower, and shall involve an additional step of removing the noise shells and filling holes at the end.

----

|

Additional Repair Features
++++++++++++++++++++++++++

.. image:: AdditionalFeaturesUpscaled.png
   :align: center

----

.. image:: removetriangles.png
   :width: 50
   :align: right

**1. Remove Small Triangles**

To remove noise shells and small floating parts.

----

.. image:: sharpTriangles.png
   :width: 50
   :align: right

**2. Filter Sharp Triangles**

To remove extremely elongated triangles.

----

.. image:: removeDupTriangles.png
   :width: 50
   :align: right

**3. Remove Duplicate Triangles**

To remove duplicate/degenerate triangles and unreferenced vertices.

----

.. image:: reduce.png
   :width: 50
   :align: right
   
**4. Reduce**

To apply triangle reduction on the mesh.

----


.. image:: unify.png
   :width: 50
   :align: right
   
**5. Unify**

To apply union boolean on the mesh.

----

.. image:: splitshells.png
   :width: 50
   :align: right

**6. Split Shells**

To split the non-intersecting shells in a mesh file.

----

.. image:: fillholes.png
   :width: 50
   :align: right

**7. Fill Holes**

To apply hole-filling operation on the mesh.

----

.. image:: smoothen.png
   :width: 50
   :align: right

**8. Smoothen**

To improve the surface smoothness of the geometry. Tick the **“Mesh Subdivision”** checkbox for better surface precision. Input the number of iterations and click on **“Smoothen”**.

.. image:: smoothen2.png
   :align: center

|

.. note:: 
   Works well only in case of uniform mesh.

----

.. image:: outerhull.png
   :width: 50
   :align: right

**9. Outer Hull**

To extract the outer hull of the geometry.

----

.. image:: remesh.png
   :width: 50
   :align: right

**10. Remesh**

To improve the surface quality of the mesh. As shown in the dialog box below, this operation needs the maximal edge size (Hmax), minimal edge size (Hmin), the edge angle to preserve and an option to smooth the surface normals of the mesh.

.. image:: remeshbefore.png
.. image:: remeshdialogbox.png
   :width: 250
.. image:: remeshafter.png
